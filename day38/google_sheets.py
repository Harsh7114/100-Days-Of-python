from pathlib import  Path
import  os
from  dotenv import  load_dotenv
from google.oauth2.service_account import  Credentials
from googleapiclient.discovery import build
Base_DIR  = Path(__file__).parent
load_dotenv(Base_DIR/".env")
SPREADSHEET_ID = os.getenv("GOOGLE_SHEET_ID")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

def get_google_sheets_service():

    credentials = Credentials.from_service_account_file(
        Base_DIR / "credentials.json",
        scopes=SCOPES
    )

    service = build(
        "sheets",
        "v4",
        credentials=credentials
    )

    return service
def add_workout(date, time, exercise, duration, calories):

    service = get_google_sheets_service()

    workout = [
        date,
        time,
        exercise,
        duration,
        calories
    ]

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range="A:E",
        valueInputOption="USER_ENTERED",
        body={
            "values": [workout]
        }
    ).execute()

    print("Workout added successfully!")