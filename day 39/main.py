from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from price_tracker import PriceTracker
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
price_tracker = PriceTracker()
notification_manager = NotificationManager()

destination_data = data_manager.get_destination_data()


today = datetime.now()

SEARCH_OFFSETS = [30, 60, 90, 120, 150, 180]

cycle_day = today.timetuple().tm_yday % len(SEARCH_OFFSETS)

days_ahead = SEARCH_OFFSETS[cycle_day]

search_date = (
    today + timedelta(days=days_ahead)
).strftime("%Y-%m-%d")


print("Days ahead:", days_ahead)
print("Searching date:", search_date)


for destination in destination_data:

    flight = flight_search.search_flight(
        destination["iataCode"],
        search_date
    )

    previous_price = price_tracker.get_previous_price(
        destination["city"],
        search_date
    )


    # -----------------------------
    # TARGET PRICE DEAL
    # -----------------------------

    if flight.price < destination["lowestPrice"]:

        message = (
            f"🔥 FLIGHT DEAL!\n\n"
            f"BLR → {flight.destination_airport}\n"
            f"{search_date}\n"
            f"₹{flight.price:,} "
            f"(Target ₹{destination['lowestPrice']:,})\n\n"
            f"{flight.airline} {flight.flight_number}\n"
            f"{flight.departure_time} → "
            f"{flight.arrival_time}\n\n"
            f"Book: {flight.flight_link}"
        )

        notification_manager.send_message(message)


    # -----------------------------
    # PRICE DROP
    # -----------------------------

    elif (
        previous_price is not None
        and flight.price < previous_price
    ):

        message = (
            f"📉 PRICE DROP!\n\n"
            f"BLR → {flight.destination_airport}\n"
            f"{search_date}\n"
            f"₹{flight.price:,} "
            f"(was ₹{previous_price:,})\n\n"
            f"{flight.airline} {flight.flight_number}\n"
            f"{flight.departure_time} → "
            f"{flight.arrival_time}\n\n"
            f"Book: {flight.flight_link}"
        )

        notification_manager.send_message(message)


    # -----------------------------
    # SAVE CURRENT PRICE
    # -----------------------------

    price_tracker.save_price(
        destination["city"],
        search_date,
        flight.price
    )


    # -----------------------------
    # TERMINAL OUTPUT
    # -----------------------------

    print(
        destination["city"],
        "| Current:", flight.price,
        "| Previous:", previous_price
    )

    print(
        destination["city"],
        "| Flight Price:", flight.price,
        "| Target Price:", destination["lowestPrice"]
    )