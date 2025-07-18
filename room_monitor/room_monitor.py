"""Room availability monitor for a single room you want to book.

More info: 
info@icebergdata.co 

This Cloud Function polls Hostelworld's availability endpoint for a *specific* room
within a property and sends you an email as soon as that room becomes available.

The implementation is intentionally very similar to the existing beach availability
checker so that you can easily understand & maintain both scripts.

Usage (when deployed as a Cloud Function):
- GET /?room_id=<ROOM_ID>&checkin=YYYY-MM-DD&nights=N
  Any of the three query-string params are optional and will fall back to the
  defaults defined below.

Environment / auxiliary files expected:
- A `config.py` sitting at project root that must define:
    passwd   – gmail / app-password string
    fromaddr – sender email address
    spid     – Google Spreadsheet ID (if you want to persist the data)
    toaddr   – *list* of destination addresses that will receive the alert
- A Google service-account credential json file (as used by the original script)

Folder structure created by this file:
project_root/
└── tips_and_tricks/
    └── room_monitor/
        └── room_monitor.py  <-- you are here
"""

import functions_framework
import json
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd
import pygsheets
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import passwd, fromaddr, spid, toaddr  # pylint: disable=import-error

# ---------------------------------------------------------------------------
# Default parameters – override them at invocation time via query-string args
# ---------------------------------------------------------------------------
PROPERTY_ID = 292988  # Costeño Beach
ROOM_ID_TO_MONITOR = 0  # Place the HW room id you want to track here
DEFAULT_CHECKIN = "2025-08-31"
DEFAULT_NIGHTS = 1
GUESTS = 2

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _fetch_availability(property_id: int, checkin: str, nights: int) -> Dict[str, Any]:
    """Call Hostelworld availability endpoint and return parsed json."""
    response = requests.get(
        url=f"https://prod.apigee.hostelworld.com/legacy-hwapi-service/2.2/properties/{property_id}/availability/",
        params={
            "guests": str(GUESTS),
            "num-nights": str(nights),
            "date-start": checkin,
            "show-rate-restrictions": "true",
            "application": "web",
        },
        headers={
            "Host": "prod.apigee.hostelworld.com",
            "Accept": "application/json, text/plain, */*",
            "api-key": "cvFkm2A4AAefXoupLsChH4jL2mA2VGSyEA0MkRUrqz8Z8x5H", #probably you need to capture another one , email info@icebergdata.co
            "User-Agent": "Mozilla/5.0",
        },
        timeout=15,
    )
    response.raise_for_status()
    return response.json()


def _flatten_rooms(raw_rooms: Dict[str, Any]) -> pd.DataFrame:
    """Return one dataframe with both dorm & private rooms concatenated."""
    frames: List[pd.DataFrame] = []
    for category in ("dorms", "privates"):
        category_rooms = raw_rooms.get(category)
        if category_rooms:
            frames.append(pd.json_normalize(category_rooms))
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def _send_email(subject: str, body_html: str) -> None:
    """Send an HTML email to all recipients in *toaddr*."""
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = ", ".join(toaddr)
    msg["Subject"] = subject
    msg.attach(MIMEText(body_html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(fromaddr, passwd)
        server.send_message(msg)


# ---------------------------------------------------------------------------
# Cloud Function entry-point
# ---------------------------------------------------------------------------

@functions_framework.http
def monitor_room(request):
    """HTTP Cloud Function to monitor a single room's availability.

    Example invocation (curl):
        curl "https://REGION-PROJECT.cloudfunctions.net/monitor_room?room_id=123456&checkin=2025-08-15&nights=2"
    """
    # Parse query params -----------------------------------------------------
    room_id = int(request.args.get("room_id", ROOM_ID_TO_MONITOR))
    checkin = request.args.get("checkin", DEFAULT_CHECKIN)
    nights = int(request.args.get("nights", DEFAULT_NIGHTS))

    if room_id == 0:
        return "Please specify ?room_id=XXXX (numeric)", 400

    # Fetch data -------------------------------------------------------------
    try:
        res_json = _fetch_availability(PROPERTY_ID, checkin, nights)
    except requests.RequestException as exc:
        return f"Error fetching availability: {exc}", 502

    rooms_df = _flatten_rooms(res_json.get("rooms", {}))
    if rooms_df.empty:
        return "No rooms returned in response", 200

    # Persist to Google Sheets (optional) ------------------------------------
    now = datetime.utcnow()
    rooms_df["date"] = now.strftime("%d/%m/%Y")
    rooms_df["time"] = now.strftime("%H:%M:%S")

    try:
        gc = pygsheets.authorize(service_file="YOURGOOGLESERVICEACCOUNT.json")
        sheet = gc.open_by_key(spid).worksheet_by_title("data")
        all_values = pd.DataFrame(sheet.get_all_values()).dropna()
        start_row = len(all_values) + 1
        sheet.set_dataframe(rooms_df, (start_row, 1), copy_head=False)
    except Exception as e:  # pylint: disable=broad-except
        # Sheets write failure should not break the function
        print(f"Warning: could not write to Google Sheets – {e}")

    # Check if the desired room is available ---------------------------------
    match = rooms_df[rooms_df["id"].astype(int) == room_id]
    if match.empty:
        print("Desired room not found in response")
        return "Room not found for given date", 200

    price = match.iloc[0].get("lowestPricePerNight.value", "?")
    ensuite_flag = match.iloc[0].get("ensuite", 0)
    ensuite_str = "Yes" if int(ensuite_flag) == 1 else "No"

    subject = "Tu habitación está disponible en Costeño Beach 🏖️"
    body = (
        f"<p>¡Buenas noticias! La habitación <b>{room_id}</b> que quieres reservar "+
        f"está disponible para el {checkin} por {nights} noche(s).</p>"
        f"<ul>"
        f"<li>Precio: <b>{price}</b></li>"
        f"<li>Baño privado: <b>{ensuite_str}</b></li>"
        f"</ul>"
        f"<p><a href='https://www.hostelworld.com/pwa/hosteldetails.php/Costeno-Beach/Guachaca/{PROPERTY_ID}?from={checkin}&to={checkin}&guests={GUESTS}&origin=microsite'>Reservar ahora</a></p>"
    )

    _send_email(subject, body)
    return "Alert sent – check your email!", 200
