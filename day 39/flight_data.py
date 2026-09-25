class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(
            self,
            price,
            origin_airport,
            destination_airport,
            departure_time,
            arrival_time,
            airline,
            flight_number,
            flight_link=None,
            booking_token=None
    ):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.airline = airline
        self.flight_number = flight_number
        self.flight_link = flight_link
        self.booking_token = booking_token
