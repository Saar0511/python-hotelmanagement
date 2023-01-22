import json


filename = "./data/Customers.json"


class Customers:
    def __init__(self, Name, Address, City, Email, Age):
        self.Name = Name
        self.Address = Address
        self.City = City
        self.Email = Email
        self.Age = Age

        #print(self.Type)

    def load_customers(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
                self.temp1 = self.temp["Rooms"]
                # print(self.temp)
                # print(len(self.temp["Customers"]))
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
        data["ID"] = len(self.temp["Customers"])
        self.temp["Customers"].append(data)
        with open(filename, "w") as f:
            json.dump(self.temp, f, indent=4)

    @classmethod
    def display_All_Customers(cls, filename="./data/Customers.json"):
        customers_list = []
        with open(filename, "r") as f:
            temp = json.load(f)
        customers_list = []
        for Customer in temp["Customers"]:
                name = Customer["Name"]
                Address = Customer["Address"]
                City = Customer["City"]
                Email = Customer["Email"]
                Age = Customer["Age"]
                ID = Customer["ID"]
                customers_list.append((name,Address,City,Email,Age,ID))
        return customers_list

    @classmethod
    def Cust_by_name(cls, name1,filename="./data/Customers.json"):

        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Customers"]
            # print(d)
            # data_length = len(temp) - 1

        # delete_option = input(f"Select id")
        for entry in d:

            if str(entry["Name"]) == str(name1):
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
               # cust = name, Address, City, Email, Age
                return Customers(name, Address, City, Email, Age)
            return "Customer not found"


            # list(filter(None, entry))


    @classmethod
    def Remove_customer(cls,delete_option):
       # new_data = []

        with open(filename, "r") as f:
            temp = json.load(f)

        for customer in temp["Customers"]:
            if customer["Name"] == delete_option:
                temp["Customers"].remove(customer)
                with open(filename, "w") as f:
                    json.dump(temp, f, indent=4)
                return True
        return False
        # for entry in d:
        #     # print(d["Name"])
        #     for custor
        #     if entry["Name"] == str(delete_option):
        #         print("yes")
        #         entry.pop()


# customer=customers("asdf","dsafasd","dsfadsf","sdf@gma.com",44,444)
# customer.view_data()
