import json
from datetime import datetime
from BookingAi import Booking

def test_Booking():
    booking = Booking(1, 1, "2022-01-15", "2022-01-20")
    assert booking.check_customer(1) == True
    assert booking.check_room(1) == True
    assert booking.check_availability(1, "2022-01-15", "2022-01-20") == True
    assert booking.TotalPrice == booking.TotalPrice
    booking.add_booking()
    
    with open("./data/Customers.json", "r") as f:
        data = json.load(f)
    assert 1 in [booking["CustID"] for booking in data["Booking"]]
    assert 1 in [booking["RoomID"] for booking in data["Booking"]]
    assert "2022-01-15" in [booking["ArrivalDate"] for booking in data["Booking"]]
    assert "2022-01-20" in [booking["DepartureDate"] for booking in data["Booking"]]
    assert 500 in [booking["TotalPrice"] for booking in data["Booking"]]

test_Booking()


