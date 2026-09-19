from flight_data import FlightData

flight = FlightData(
    price=7747,
    origin_airport="BLR",
    destination_airport="PAT"
)

print(flight.price)
print(flight.origin_airport)
print(flight.destination_airport)