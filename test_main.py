import unittest
import json
from main import Rooms

class TestMain(unittest.TestCase):
    def test_add_room(self):
        room = Rooms("22mr", 10, 2, "Basic", 100)
        room.Add_room()
        with open("./data/Customers.json", "r") as f:
            data = json.load(f)
            self.assertEqual(len(data["Rooms"]), (len(data["Rooms"])))
            self.assertEqual(data["Rooms"][0]["Size"], "22mr")
            self.assertEqual(data["Rooms"][0]["Capacity"], 10)
            self.assertEqual(data["Rooms"][0]["NumberOfBeds"], 2)
            self.assertEqual(data["Rooms"][0]["Type"], "Basic")
            self.assertEqual(data["Rooms"][0]["Price"], 100)

if __name__ == '__main__':
    unittest.main()