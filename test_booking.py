import unittest
from BookingAi import Booking

class TestBooking(unittest.TestCase):

     def setUp(self):
         self.booking = Booking(1, 1, "2022-01-01", "2022-01-05")
         self.booking2 = Booking(1, 1, "2022-01-01", "2022-01-02")
         self.booking3 = Booking(2, 2, "2022-01-01", "2022-01-05")
         self.booking4 = Booking(1, 2, "2022-01-01", "2022-01-05")

     def test_check_customer(self):
         self.assertTrue(self.booking.check_customer(1))
         self.assertTrue(self.booking.check_customer(2))

     def test_check_room(self):
         self.assertTrue(self.booking.check_room(1))
         self.assertTrue(self.booking.check_room(2))

     def test_check_availability(self):
         self.assertFalse(self.booking.check_availability(1, "2022-01-01", "2022-01-05"))
         self.assertFalse(self.booking.check_availability(1, "2022-01-01", "2022-01-05"))
         self.assertTrue(self.booking3.check_availability(2, "2022-01-01", "2022-01-05"))
         self.assertTrue(self.booking4.check_availability(2, "2022-01-01", "2022-01-05"))

     def test_set_total_price(self):
         self.booking.set_total_price()
         self.assertEqual(self.booking.TotalPrice, 400)

     def test_add_booking(self):
         self.booking.add_booking()
         self.assertFalse(self.booking.check_availability(1, "2022-01-01", "2022-01-05"))
         self.assertFalse(self.booking2.check_availability(1, "2022-01-01", "2022-01-02"))
unittest.main()