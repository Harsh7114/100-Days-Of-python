import os
import requests
from pathlib  import  Path
from dotenv import  load_dotenv
BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR/".env")

class FlightSearch:
    CITY_CODES = {
        "Mumbai": "BOM",
        "Delhi": "DEL",
        "Patna": "PAT",
        "Varanasi": "VNS",
        "Jaipur": "JAI",
        "Pune": "PNQ",
        "Goa": "GOI",
    }

    def __init__(self):
        self.serpapi_key = os.getenv("SERPAPI_KEY")

        if not self.serpapi_key:
            raise ValueError("SERPAPI_KEY not found in .env")

    def get_destination_code(self, city):
        city = city.strip()
        return self.CITY_CODES.get(city)

    def search_flight(self, destination):
        url = "https://serpapi.com/search"

        params = {
            "engine": "google_flights",
            "departure_id": "BLR",
            "arrival_id": destination,
            "outbound_date": "2026-10-06",
            "currency": "INR",
            "hl": "en",
            "adults": 1,
            "type": "2",
            "api_key": self.serpapi_key
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        return data