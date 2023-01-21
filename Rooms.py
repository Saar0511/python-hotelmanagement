import json

filename = "./data/Customers.json"


class Rooms:
    def __init__(self, size, capacity, numberOfBeds, Type, price):

        self._Size = size
        self._Capacity = capacity
        self._NumberOfBeds = numberOfBeds
        self._Type = Type
        self._Price = price

    def load_rooms(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
        except Exception as error:
            print(f"Couldn't load the file - error {error}")

    def set_min_booking_time(self):
        if self._Type == "Basic":
            return 1
        elif self._Type == "Deluxe":
            return 2
        elif self._Type == "Suite":
            return 3

    @classmethod
    def display_All_Rooms(cls):
        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Rooms"]
            de=[]
            for entry in d:
                ID = entry["id"]
                Size = entry["Size"]
                Capacity = entry["Capacity"]
                NumberOfBeds = entry["NumberOfBeds"]
                Type = entry["Type"]
                Price = entry["Price"]

                de.append((f"Room Number {ID}"),
                (f"Size of The Room  : {Size}"),
                (f"Capacity of Rom: {Capacity}"),
                (f"NumberOfBeds in the Room  : {NumberOfBeds}"),
                (f"Type of the room  : {Type}"),
                (f"Price of the Room  : {Price}"),
                ("\n\n"))

                return json.dumps(de)


    def Add_room(self):
        self.load_rooms()
        data = {}
        data["id"] = len(self.temp["Rooms"]) + 1
        data["Size"] = self._Size
        data["Capacity"] = self._Capacity
        data["NumberOfBeds"] = self._NumberOfBeds
        data["Type"] = self._Type
        data["Price"] = self._Price

        self.temp["Rooms"].append(data)
        with open(filename, "w") as f:
            json.dump(self.temp, f, indent=4)

    def Book_room(self):
        self.load_rooms()
        print(self.temp)
        data = {}
        data["CustID"] = self.CustID
        data["RoomID"] = self._id
        data["ArrivalDate"] = self.ArrivalDate
        data["DepartureDate"] = self.DepartureDate
        data["TotalPrice"] = self.TotalPrice

        self.temp["Booking"].append(data)
        with open(filename, "w") as f:
            json.dump(self.temp, f, indent=4)
    @classmethod
    def RoomByType(cls,filename="./data/Customers.json"):


        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Rooms"]
        room_type = input("Enter room type (Basic, Deluxe, Suite): ")
        delete_option = room_type
        for entry in d:

            if entry["Type"] == str(delete_option):
                ID = entry["id"]
                Size = entry["Size"]
                Capacity = entry["Capacity"]
                NumberOfBeds = entry["NumberOfBeds"]
                Type = entry["Type"]
                Price = entry["Price"]
                print(f"Room Number {ID}")
                print(f"Size of The Room  : {Size}")
                print(f"Capacity of Rom: {Capacity}")
                print(f"NumberOfBeds in the Room  : {NumberOfBeds}")
                print(f"Type of the room  : {Type}")
                print(f"Price of the Room  : {Price}")
                print("\n\n")
            else:
                pass
    @classmethod
    def RoomByNumber(cls, filename="./data/Customers.json"):

        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Rooms"]
        room_number = input("Enter room number: ")
        for entry in d:

            if int(entry["id"]) == int(room_number):
                ID = entry["id"]
                Size = entry["Size"]
                Capacity = entry["Capacity"]
                NumberOfBeds = entry["NumberOfBeds"]
                Type = entry["Type"]
                Price = entry["Price"]
                print(f"Room Number {ID}")
                print(f"Size of The Room  : {Size}")
                print(f"Capacity of Rom: {Capacity}")
                print(f"NumberOfBeds in the Room  : {NumberOfBeds}")
                print(f"Type of the room  : {Type}")
                print(f"Price of the Room  : {Price}")
                print("\n\n")
            else:
                pass

    @classmethod
    def Remove_Room(cls):

            with open(filename, "r") as f:
                temp = json.load(f)
            print("Which Room would you like to delete?")
            delete_option = int(input(f"Select a Room Number"))

            for Room in temp["Rooms"]:
                if Room["id"] == delete_option:
                    temp["Rooms"].remove(Room)
                    with open(filename, "w") as f:
                        json.dump(temp, f, indent=4)
                    return "Room removed successfully"

            return "No Room found By This Room Number"