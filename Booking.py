import json
from datetime import datetime as dt

filename = "./data/Customers.json"


class Booking:

    def __init__(self, ArrivalDate, DepartureDate, CustID, RoomID):
        self.ArrivalDate = ArrivalDate
        self.DepartureDate = DepartureDate
        self.CustID = CustID
        self.RoomID = RoomID
        #self.total_price = total_price

    def load_data(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
        except Exception as error:
            print(f"Couldn't load the file - error {error}")

    def check_customer(self, cust_id):
        self.load_data()
        for customer in self.temp["Customers"]:
            if customer["ID"] == cust_id:
                return True
        return False

    def check_room(self, room_id):
        self.load_data()
        for room in self.temp["Rooms"]:
            if room["id"] == room_id:
                return True
        return False

    def cancel_booking(self, cust_id, room_id):
        self.load_data()
        for booking in self.temp["Booking"]:
            if booking["CustID"] == cust_id and booking["RoomID"] == room_id:
                self.temp["Booking"].remove(booking)
                with open(filename, "w") as f:
                    json.dump(self.temp, f, indent=4)
                print("Booking canceled successfully.")
                return
        print("Booking not found.")

    def check_availability(self, room_id, arrival_date, departure_date):
        self.load_data()
        for booking in self.temp["Booking"]:
            if booking["RoomID"] == room_id and (
                    arrival_date >= booking["ArrivalDate"] and arrival_date <= booking["DepartureDate"]) or (
                    departure_date >= booking["ArrivalDate"] and departure_date <= booking["DepartureDate"]):
                return False
        return True

    def make_booking(self, cust_id, room_id, arrival_date, departure_date, total_price):
        if self.check_customer(cust_id) and self.check_room(room_id) and self.check_availability(room_id, arrival_date,
                                                                                                 departure_date):
            data = {}
            data["CustID"] = cust_id
            data["RoomID"] = room_id
            data["ArrivalDate"] = arrival_date
            data["DepartureDate"] = departure_date
            data["TotalPrice"] = self.TotalPrice()
            self.temp["Booking"].append(data)
            with open(filename, "w") as f:
                json.dump(self.temp, f, indent=4)
            print("Booking successful!")
        else:
            print("Booking failed, please check the customer ID, room ID and availability.")
    # def get_customer_by_id(self, filename="./data/Customers.json",):
    #     try:
    #         with open(filename, "r") as f:
    #             self.temp = json.load(f)
    #             self.Customers=self.temp["Customers"]
    #             for customer in self.Customers:
    #                 if customer["id"] == ID:
    #                     return customer
    #                 return None

    # except Exception as error:
    #     print(f"Couldn't load the file - error {error}")

    def load_Booking(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)
                self.Book = self.temp["Booking"]
                # self.temp1 = self.temp["Booking"]
                # print(self.temp)
                # print(len(self.temp["Customers"]))
        except Exception as error:
            print(f"Couldn't load the file - error {error}")

    @classmethod
    def View_All_Booking(cls):
        with open(filename, "r") as f:
            temp = json.load(f)
            d = temp["Booking"]
            # print(d)
            # data_length = len(temp) - 1
        for entry in d:

            CustID = entry["CustID"]
            RoomID = entry["RoomID"]
            ArrivalDate = entry["ArrivalDate"]
            DepartureDate = entry["DepartureDate"]
            TotalPrice = entry["TotalPrice"]
            print(f"Room Number {RoomID}")
            print(f"Customer ID is : {CustID}")
            print(f"ArrivalDate is: {ArrivalDate}")
            print(f"DepartureDate is  : {DepartureDate}")
            print(f"TotalPrice is  : {TotalPrice}")
            print("\n\n")
            # list(filter(None, entry))

        else:
            pass

    # def display_booked_rooms_for_date(bookings, date):

    def Book_Room(self):
        data = {}
        with open(filename, 'r', encoding='utf-8') as f:
            temp = json.load(f)
        # data1 = temp['Rooms']
        # print(data)
        data["CustID"] = self.CustID
        data["RoomNumber"] = self.RoomID
        data["ArrivalTime"] = self.ArrivalDate
        data["DepartureDate"] = self.DepartureDate
        data["TotalPrice"] = self.TotalPrice()
        if  temp["Rooms"]["id"]==self.RoomID:
            temp["Rooms"]["Price"] = self.price

        temp["Booking"].append(data)
        with open(filename, "w") as f:
            json.dump(temp, f, indent=4)

    def TotalDays(self):
        print("hh")
        self.TotalDays = (dt.strptime(self.DepartureDate, "%d/%m/%Y") - dt.strptime(self.ArrivalDate, "%d/%m/%Y")).days
        print(self.TotalDays)

    def TotalPrice(self):
        self.TotalPrice = self.price * self.TotalDays
        return self.TotalPrice

    def __str__(self):
        return f"the total days is{self.TotalDays} and the price is{self.TotalPrice1}"

book = Booking('15/10/2023', '20/2/2023',1,1)
#print(#datetime.utcnow())
book.make_booking()
# book.TotalDays1()
