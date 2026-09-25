import os
import requests
from pathlib import Path
from dotenv import load_dotenv

from flight_data import FlightData


BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")


class FlightSearch:

    def __init__(self):
        self.serpapi_key = os.getenv("SERPAPI_KEY")

        if not self.serpapi_key:
            raise ValueError("SERPAPI_KEY not found in .env")

    def search_flight(self, destination, date):

        url = "https://serpapi.com/search"

        params = {
            "engine": "google_flights",
            "departure_id": "BLR",
            "arrival_id": destination,
            "outbound_date": date,
            "currency": "INR",
            "hl": "en",
            "adults": 1,
            "type": "2",
            "api_key": self.serpapi_key
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        best_flights = data.get("best_flights", [])
        other_flights = data.get("other_flights", [])

        all_flights = best_flights + other_flights

        flights_with_price = [
            flight
            for flight in all_flights
            if "price" in flight
        ]

        if not flights_with_price:
            raise ValueError(
                f"No priced flights found for {destination} on {date}"
            )

        cheapest_flight = min(
            flights_with_price,
            key=lambda flight: flight["price"]
        )

        price = cheapest_flight["price"]

        first_segment = cheapest_flight["flights"][0]
        last_segment = cheapest_flight["flights"][-1]

        airline = first_segment["airline"]
        flight_number = first_segment["flight_number"]

        origin_airport = first_segment["departure_airport"]["id"]
        destination_airport = last_segment["arrival_airport"]["id"]

        departure_time = first_segment["departure_airport"]["time"]
        arrival_time = last_segment["arrival_airport"]["time"]

        flight_link = self.get_google_flights_link(
            destination,
            date
        )

        return FlightData(
            price=price,
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            departure_time=departure_time,
            arrival_time=arrival_time,
            airline=airline,
            flight_number=flight_number,
            flight_link=flight_link
        )

    def get_google_flights_link(self, arrival_id, outbound_date):

        return (
            f"https://www.google.com/travel/flights?"
            f"q=Flights%20from%20BLR%20to%20{arrival_id}"
            f"%20on%20{outbound_date}"
        )