"""Project-wide configuration variables.

Fill in the values below with your own credentials. This file is *ignored* by
version-control by default (add it to your .gitignore) so that private keys and
passwords are not committed to your repository.
"""

# Gmail SMTP -----------------------------------------------------------------
# Generate an "App Password" in your Google account security settings and place
# it here. Do *not* use your regular Gmail password.
passwd: str = "YOUR_GMAIL_APP_PASSWORD"

# Sender e-mail address (typically the same account that owns the app password)
fromaddr: str = "you@example.com"

# List of e-mail addresses to notify when a new room is available.
toaddr: list[str] = [
    "you@example.com",
    # "friend@example.com",
]

# Google Sheets --------------------------------------------------------------
# Spreadsheet ID where availability checks are logged. Leave blank if you do
# not want to store data.
spid: str | None = "YOUR_GOOGLE_SHEET_ID"

# ---------------------------------------------------------------------------
# End of config.py
