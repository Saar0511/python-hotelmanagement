import json

filename = "./data/Customers.json"


class Rooms:
    def __init__(self, size, capacity, numberOfBeds, Type, price):

        self._Size = size
        self._Capacity = capacity
        self._NumberOfBeds = numberOfBeds
        self._Type = Type
        self._Price = price
        # print(self._id())

    # self._room_type = {"Basic": 1, "Delux": 2, "Suite": 3}

    def load_rooms(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
                # self.temp1 = self.temp["Rooms"]
                # print(self.temp)
                #print(len(self.temp["Customers"]))
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
                # i = i + 1


    # pass

    def Add_room(self):
        self.load_rooms()
        # print(self.temp)
        data = {}
        data["id"] = len(self.temp["Rooms"]) + 1
        data["Size"] = self._Size
        data["Capacity"] = self._Capacity
        data["NumberOfBeds"] = self._NumberOfBeds
        data["Type"] = self._Type
        data["Price"] = self._Price
        # temp["Rooms"]

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

        # temp["Rooms"]

        self.temp["Booking"].append(data)
        with open(filename, "w") as f:
            json.dump(self.temp, f, indent=4)
    @classmethod
    def RoomByType(cls,filename="./data/Customers.json"):
        # self.Display_All()
        # new_data = []

        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Rooms"]
            # print(d)
            # data_length = len(temp) - 1
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
            # list(filter(None, entry))

            else:
                pass
    @classmethod
    def RoomByNumber(cls, filename="./data/Customers.json"):

        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Rooms"]
            # print(d)
            # data_length = len(temp) - 1
        room_number = input("Enter room number: ")
       # delete_option = input(f"Select id")
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

            # list(filter(None, entry))

            else:
                pass

    @classmethod
    def Remove_Room(cls):

            with open(filename, "r") as f:
                temp = json.load(f)
                # d = temp["Customers"]
                # print(d)
                # data_length = len(temp) - 1
            print("Which Room would you like to delete?")
            delete_option = int(input(f"Select a Room Number"))

            for Room in temp["Rooms"]:
                if Room["id"] == delete_option:
                    temp["Rooms"].remove(Room)
                    with open(filename, "w") as f:
                        json.dump(temp, f, indent=4)
                    return "Room removed successfully"

            return "No Room found By This Room Number"

#
# #C = Customer.Customers()
# #C.inputdata()
# Room1 = Rooms(55, 100, 150, 15, "Basic", 100)
# Room1.load_rooms()
# Room1.Add_room()
# # Room1.RoomByType()
# # Room1.RoomByNumber()
# # Room1.display_All_Rooms()
