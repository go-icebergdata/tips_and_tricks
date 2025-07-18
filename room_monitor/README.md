# Room Monitor – Costeño Beach

![Room Monitor](2021-06-28.webp)

This Cloud Function checks the availability of **one specific room** at Costeño Beach (or any other Hostelworld property) and notifies you via e-mail the moment it becomes available.

## Features

* Polls Hostelworld JSON availability endpoint.
* Persists every check to a Google Sheet for later analysis.
* Sends an HTML email (Gmail SMTP) with price, ensuite flag and a direct booking link when the target room appears.
* Configurable at invocation time via query-string parameters.

## Folder structure
```
project_root/
└── tips_and_tricks/
    └── room_monitor/
        ├── room_monitor.py   # Cloud Function code
        └── README.md         # you are here
```

## Prerequisites

1. **Google Cloud Functions** runtime (Python 3.10 or similar).
2. A Gmail account with an *App Password* enabled.
3. `config.py` at project root that defines:
   ```python
   passwd   = "<gmail-app-password>"
   fromaddr = "you@gmail.com"
   spid     = "<google-sheet-id>"  # optional – leave blank to skip sheet write
   toaddr   = ["you@gmail.com", "friend@example.com"]
   ```
4. Google Sheets service-account credentials json (`bakingmeal-779aade390a7.json`) if you want spreadsheet logging.

## Quick deploy (gcloud CLI)

```bash
 gcloud functions deploy monitor_room \
   --runtime python310 \
   --trigger-http \
   --region <REGION> \
   --entry-point monitor_room \
   --source tips_and_tricks/room_monitor \
   --allow-unauthenticated
```

## Invocation examples

1. **Default parameters** (uses the `ROOM_ID_TO_MONITOR` constant in the code):
   ```
   https://REGION-PROJECT.cloudfunctions.net/monitor_room
   ```
2. **Override room ID, date & nights**:
   ```
   https://REGION-PROJECT.cloudfunctions.net/monitor_room?room_id=123456&checkin=2025-08-15&nights=2
   ```

## Customisation

* Change `PROPERTY_ID` to monitor a different hostel.
* Default `ROOM_ID_TO_MONITOR`, `DEFAULT_CHECKIN`, and `DEFAULT_NIGHTS` can be edited in `room_monitor.py`.
* If you don’t need Google Sheets logging, simply remove or comment out the block labelled “Persist to Google Sheets”.

## Local testing

Create a Python virtualenv and install dependencies:
```bash
pip install -r requirements.txt  # pandas, pygsheets, requests, functions-framework, etc.
functions-framework --target monitor_room --port 8080
```
Then hit `http://localhost:8080/?room_id=123456&checkin=2025-08-15&nights=2` in your browser or with `curl`.

---
**Enjoy your stay! 🏖️**
