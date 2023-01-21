#from Rooms import Rooms
import json

filename = "./data/Customers.json"


class Customers:
    def __init__(self, Name, Address, City, Email, Age):
        self.Name = Name
        self.Address = Address
        self.City = City
        self.Email = Email
        self.Age = Age

    def load_rooms(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
                #self.temp1 = self.temp["Rooms"]
                # print(self.temp)
                #print(len(self.temp["Customers"]))
        except Exception as error:
            print(f"Couldn't load the file - error {error}")

    def Add_customer(self):
        data = {}
        with open(filename, 'r', encoding='utf-8') as f:
            temp = json.load(f)
        #data1 = temp['Rooms']
        # print(data)
        data["Name"] = self.Name
        data["Address"] = self.Address
        data["City"] = self.City
        data["Email"] = self.Email
        data["Age"] = self.Age
        data["id"] = len(self.temp["Customers"])
        # temp["Rooms"]

        temp["Customers"].append(data)
        with open(filename, "w") as f:
            json.dump(temp, f, indent=4)

    def Display_All(self):
        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Customers"]
            i = 0
            for entry in d:
                Name = entry["Name"]
                Address = entry["Address"]
                City = entry["City"]
                Email = entry["Email"]
                Age = entry["Age"]
                print(f"Room Number {i}")
                print(f"Name of Customer  : {Name}")
                print(f"Address of Customer: {Address}")
                print(f"City of customer  : {City}")
                print(f"Email of customer  : {Email}")
                print(f"Age of customer  : {Age}")

                print("\n\n")
                i = i + 1
    @classmethod
    def Remove_customer(cls):
       # new_data = []

        with open(filename, "r") as f:
            temp = json.load(f)
            #d = temp["Customers"]
            #print(d)
            #data_length = len(temp) - 1
        print("Which Customer would you like to delete?")
        delete_option = input(f"Select a Customer Name")
        i = 0
        for entry in temp:
            # print(d["Name"])
            if entry["Customers"]["Name"] == str(delete_option):
                print("yes")
                entry.clear()
               # list(filter(None, entry))

            else:
                pass
                #temp.append(entry)

        with open(filename, "w") as f:
            for entry in d:
                #print(entry)
                if entry == {}:
                    print("kk")
                    temp.clear(entry)


            json.dump(temp, f, indent=4)

    @classmethod
    def find(cls, filename="./data/Customers.json"):

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

            # list(filter(None, entry))

            else:
                pass


#
#customer = Customers()
# customer.inputdata()
#customer.Display_All()
#customer.Remove_customer()
#room = Rooms(Pk = 123)