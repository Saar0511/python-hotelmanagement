import json


filename = "./data/Customers.json"


class Customers:
    def __init__(self, Name, Address, City, Email, Age):
        self.Name = Name
        self.Address = Address
        self.City = City
        self.Email = Email
        self.Age = Age

    def load_customers(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
                self.temp1 = self.temp["Rooms"]
        except Exception as error:
            print(f"Couldn't load the file - error {error}")

    def add_data(self):
        self.load_customers()
        data = {}


        data["Name"] = self.Name
        data["Address"] = self.Address
        data["City"] = self.City
        data["Email"] = self.Email
        data["Age"] = self.Age
        data["ID"] = len(self.temp["Customers"]) + 1
        self.temp["Customers"].append(data)
        with open(filename, "w") as f:
            json.dump(self.temp, f, indent=4)

    @classmethod
    def view_data(cls):

        with open(filename, "r", encoding='utf-8') as f:
            temp = json.load(f)
            d=temp["Customers"]
            for entry in d:
                name = entry["Name"]
                Address = entry["Address"]
                City = entry["City"]
                Email = entry["Email"]
                Age = entry["Age"]
                ID = entry["ID"]
                print(f"Customer id {ID}")
                print(f"Name of custumer  : {name}")
                print(f"Adress of custumer: {Address}")
                print(f"City of custumer  : {City}")
                print(f"Email of custumer  : {Email}")
                print(f"Age of custumer  : {Age}")
                print("\n\n")

    @classmethod
    def Cust_by_name(cls, filename="./data/Customers.json"):

        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Customers"]
        Customer_Name = input("Enter Customer Name: ")
        for entry in d:

            if str(entry["Name"]) == str(Customer_Name):
                name = entry["Name"]
                Address = entry["Address"]
                City = entry["City"]
                Email = entry["Email"]
                Age = entry["Age"]
                ID = entry["ID"]
                print(f"Customer id {ID}")
                print(f"Name of custumer  : {name}")
                print(f"Adress of custumer: {Address}")
                print(f"City of custumer  : {City}")
                print(f"Email of custumer  : {Email}")
                print(f"Age of custumer  : {Age}")
                print("\n\n")

            else:
                pass
    @classmethod
    def Remove_customer(cls,name):
        with open(filename, "r") as f:
            temp = json.load(f)
        
        name = input(f"Select a Customer Name")
        i = 0

        for customer in temp["Customers"]:
            if customer["Name"] == name:
                temp["Customers"].remove(customer)
                with open(filename, "w") as f:
                    json.dump(temp, f, indent=4)
                return "Customer removed successfully"

        return "No customer found with the given name"