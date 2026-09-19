class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin_airport,destination_airport):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport