import json
from pathlib import Path
from datetime import datetime


class PriceTracker:

    def __init__(self):
        self.file_path = Path(__file__).parent / "price_history.json"

    def load_history(self):
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_price(self, city, travel_date, price):

        history = self.load_history()

        history.append({
            "checked_date": datetime.now().strftime("%Y-%m-%d"),
            "city": city,
            "travel_date": travel_date,
            "price": price
        })

        with open(self.file_path, "w") as file:
            json.dump(history, file, indent=4)

    def get_previous_price(self, city, travel_date):

        history = self.load_history()

        for record in reversed(history):
            if (
                record["city"].strip() == city.strip()
                and record["travel_date"] == travel_date
            ):
                return record["price"]

        return None