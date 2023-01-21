from Booking import Booking
def test_booking():
    # Test checking if a customer exists
    booking = Booking(1, 1, "01/01/2021", "05/01/2021")
    assert booking.check_customer(1) == True
    assert booking.check_customer(1000) == False
    
    # Test checking if a room exists
    assert booking.check_room(1) == True
    assert booking.check_room(1000) == False
    
    # Test checking room availability
    #assert booking.check_availability(1, "01/01/2021", "05/01/2021") == True
    #assert booking.check_availability(1, "01/01/2021", "05/01/2022") == False
    
    # Test setting the total price of the booking
    booking.set_total_price()
    assert booking.TotalPrice > 0
    
    # Test adding a new booking
    booking.add_booking()
    booking.load_data()
    assert len(booking.temp["Booking"]) == len(booking.temp["Booking"])
    #assert booking.temp["Booking"][0]["TotalPrice"] == booking.TotalPrice
    
test_booking()

