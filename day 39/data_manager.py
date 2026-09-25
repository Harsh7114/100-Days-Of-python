import os
import requests
from pathlib import  Path
Base_DIR  = Path(__file__).parent

from dotenv import load_dotenv
load_dotenv(Base_DIR/".env")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        if not self.sheety_endpoint:
            raise ValueError("SHEETY_ENDPOINT not found in .env")

    def get_destination_data(self):
        response = requests.get(url=self.sheety_endpoint)
        response.raise_for_status()

        data = response.json()
        return data["sheet1"]

    def update_destination_code(self, row_id, iata_code):
        body = {
            "sheet1": {
                "iataCode": iata_code
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.put(
            url=f"{self.sheety_endpoint}/{row_id}",
            json=body,
            headers=headers
        )

        response.raise_for_status()
