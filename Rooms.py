import json

filename = "./data/Customers.json"


class Rooms:
    def __init__(self, size, capacity, numberOfBeds, Type, price):

        self.Size = size
        self.Capacity = capacity
        self.NumberOfBeds = numberOfBeds
        self.Type = Type
        self.Price = price

    # self._room_type = {"Basic": 1, "Delux": 2, "Suite": 3}

    def load_rooms(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
                # self.temp1 = self.temp["Rooms"]
                # print(self.temp)
                # print(len(self.temp["Customers"]))
        except Exception as error:
            print(f"Couldn't load the file - error {error}")

    @classmethod
    def display_All_Rooms(cls):

        with open(filename, "r") as f:
            temp = json.load(f)
            #d = temp["Rooms"]
        rooms_list = []
        for Room in temp["Rooms"]:
                ID = Room["id"]
                size = Room["Size"]
                Capacity = Room["Capacity"]
                NumberOfBeds = Room["NumberOfBeds"]
                Type = Room["Type"]
                Price = Room["Price"]

                rooms_list.append((ID, size, Capacity, NumberOfBeds, Type, Price))
        return rooms_list

    # pass

    def Add_room(self):
        self.load_rooms()
        # print(self.temp)
        data = {}
        data["id"] = len(self.temp["Rooms"]) + 1
        data["Size"] = self.Size
        data["Capacity"] = self.Capacity
        data["NumberOfBeds"] = self.NumberOfBeds
        data["Type"] = self.Type
        data["Price"] = self.Price
        # temp["Rooms"]

        self.temp["Rooms"].append(data)
        with open(filename, "w") as f:
            json.dump(self.temp, f, indent=4)
        return True

    # def Book_room(self):
    #     self.load_rooms()
    #     print(self.temp)
    #     data = {}
    #     data["CustID"] = self.CustID
    #     data["RoomID"] = self.ID
    #     data["ArrivalDate"] = self.ArrivalDate
    #     data["DepartureDate"] = self.DepartureDate
    #     data["TotalPrice"] = self.TotalPrice
    #
    #     # temp["Rooms"]
    #
    #     self.temp["Booking"].append(data)
    #     with open(filename, "w") as f:
    #         json.dump(self.temp, f, indent=4)

    @classmethod
    def RoomByType(cls,room_type, filename="./data/Customers.json"):
        # self.Display_All()
        # new_data = []
        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Rooms"]
        rooms_list=[]
            # print(d)
            # data_length = len(temp) - 1

        for entry in d:

            if entry["Type"] == str(room_type):
                ID = entry["id"]
                Size = entry["Size"]
                Capacity = entry["Capacity"]
                NumberOfBeds = entry["NumberOfBeds"]
                Type = entry["Type"]
                Price = entry["Price"]
                rooms_list.append((ID, Size, Capacity, NumberOfBeds, Type, Price))

            # list(filter(None, entry)
        if len(rooms_list)>0:
            return rooms_list
        else:
            return False

    @classmethod
    def RoomByNumber(cls, room_number, filename="./data/Customers.json"):

        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Rooms"]
        for entry in d:

            if int(entry["id"]) == int(room_number):
                ID = entry["id"]
                Size = entry["Size"]
                Capacity = entry["Capacity"]
                NumberOfBeds = entry["NumberOfBeds"]
                Type = entry["Type"]
                Price = entry["Price"]

                return Rooms(Size, Capacity, NumberOfBeds, Type, Price)

            # list(filter(None, entry))

            else:
                pass

    @classmethod
    def Remove_Room(cls,delete_option):

        with open(filename, "r") as f:
            temp = json.load(f)
            # d = temp["Customers"]
            # print(d)
            # data_length = len(temp) - 1
        deleted = False
        for Room in temp["Rooms"]:
            if Room["id"] == delete_option:
                temp["Rooms"].remove(Room)
                deleted = True
                break
        if deleted:
            with open(filename, "w") as f:
                json.dump(temp, f, indent=4)
            return True
        else:
            return False

    def __str__(self):
        return f"Size: {self.Size}, Capacity: {self.Capacity}, Number of Beds: {self.NumberOfBeds}, Type: {self.Type}, Price: {self.Price}"

#
# #C = Customer.Customers()
# #C.inputdata()
# Room1 = Rooms(55, 100, 150, 15, "Basic", 100)
# Room1.load_rooms()
# Room1.Add_room()
# # Room1.RoomByType()
# # Room1.RoomByNumber()
# # Room1.display_All_Rooms()
