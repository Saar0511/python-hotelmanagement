import unittest
from Rooms import Rooms


class TestRooms(unittest.TestCase):

    def setUp(self):
        self.room1 = Rooms(size="22mr", capacity=10,
                           numberOfBeds=2, Type='Basic', price=100)
        self.room2 = Rooms(size="26mr", capacity=10,
                           numberOfBeds=2, Type='Deluxe', price=200)
        self.room3 = Rooms(size="30mr", capacity=10,
                           numberOfBeds=4, Type='Suite', price=300)

    def test_add_room(self):
        self.room1.Add_room()
        self.room2.Add_room()
        self.room3.Add_room()

    def test_display_all_rooms(self):
        Room = Rooms.display_All_Rooms()
        for R in Room:
                ID = R[0]
                Size = R[1]
                Capacity = R[2]
                NumberOfBeds = R[3]
                Type = R[4]
                Price = R[5]
                print(f"Room Number: {ID}")
                print(f"Size Of The Room is: {Size}")
                print(f"Room type: {Type}")
                print(f"Capacity: {Capacity}")
                print(f"NumberOfBeds: {NumberOfBeds}")
                print(f"Price: {Price}\n\n\n")
                print("")
            


    def test_room_by_type(self):
        Rooms.RoomByType()


if __name__ == '__main__':
    unittest.main()
