import unittest


class TestRoomsMethods(unittest.TestCase):
    def setUp(self):


        self.room = Rooms(size=20, capacity=2, numberOfBeds=1, Type='Basic', price=30)
        self.booking = {
        "CustID": 1,
        "RoomID": 1,
        "ArrivalDate": "2022-01-01",
        "DepartureDate": "2022-01-03",
        "TotalPrice": 90
        }


def test_load_rooms(self):
    self.room.load_rooms()
    self.assertIsNotNone(self.room.temp)


def test_set_min_booking_time(self):
    self.assertEqual(self.room.set_min_booking_time(), 1)


def test_display_all_rooms(self):
    self.assertIsNotNone(self.room.display_All_Rooms())


def test_add_room(self):
    self.room.Add_room()
    with open(filename, "r") as f:
        temp = json.load(f)
        self.assertEqual(len(temp["Rooms"]), 1)


def test_book_room(self):
    self.room.Book_room()
    with open(filename, "r") as f:
        temp = json.load(f)
        self.assertEqual(temp["Booking"][0], self.booking)


def test_room_by_type(self):
    self.room.RoomByType()
    with open(filename, "r") as f:
        temp = json.load(f)
        self.assertEqual(temp["Rooms"][0]["Type"], 'Basic')


if __name__ == '__main__':
    unittest.main()