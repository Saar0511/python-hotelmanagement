import json
from datetime import datetime

filename = "./data/Customers.json"


class Booking:
    def __init__(self, CustID, RoomID, ArrivalDate, DepartureDate):
        self.CustID = CustID
        self.RoomID = RoomID
        self.ArrivalDate = ArrivalDate
        self.DepartureDate = DepartureDate
        self.TotalPrice = 0

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

    def check_availability(self, room_id, arrival_date, departure_date):
        self.load_data()
        arrival_date = datetime.strptime(arrival_date, "%d/%m/%Y")
        departure_date = datetime.strptime(departure_date, "%d/%m/%Y")
        for booking in self.temp["Booking"]:
            if booking["RoomID"] == room_id and (
                    arrival_date >= datetime.strptime(booking["ArrivalDate"], "%d/%m/%Y") and
                    arrival_date <= datetime.strptime(booking["DepartureDate"], "%d/%m/%Y")) or (
                    departure_date >= datetime.strptime(booking["ArrivalDate"], "%d/%m/%Y") and
                    departure_date <= datetime.strptime(booking["DepartureDate"], "%d/%m/%Y")):
                return False
        nights = (departure_date - arrival_date).days
        room_type = None
        for room in self.temp["Rooms"]:
            if room["id"] == room_id:
                room_type = room["Type"]
                break
        if room_type == "Deluxe":
            if nights < 2:
                print("Minimum stay for deluxe room is 2 nights.")
                return False
        if room_type == "Suite":
            if nights < 3:
                print("Minimum stay for suite room is 3 nights.")
                return False
        return True

    def load_data(self, filename="./data/Customers.json"):
        try:
            with open(filename, "r") as f:
                self.temp = json.load(f)

        except Exception as error:
            print(f"Couldn't load the file - error {error}")

    def set_total_price(self):
        self.load_data()
        room = None
        for r in self.temp["Rooms"]:
            if r["id"] == self.RoomID:
                room = r
                break
        if room:
            arrival = datetime.strptime(self.ArrivalDate, "%d/%m/%Y")
            departure = datetime.strptime(self.DepartureDate, "%d/%m/%Y")
            nights = (departure - arrival).days
            self.TotalPrice = nights * room["Price"]

    def add_booking(self):

        if self.check_customer(self.CustID) and self.check_room(self.RoomID) and self.check_availability(self.RoomID,
                                                                                                         self.ArrivalDate,
                                                                                                         self.DepartureDate):
            self.load_data()
            self.set_total_price()
            data = {}
            data["CustID"] = self.CustID
            data["RoomID"] = self.RoomID
            data["ArrivalDate"] = self.ArrivalDate
            data["DepartureDate"] = self.DepartureDate
            data["TotalPrice"] = self.TotalPrice
            self.temp["Booking"].append(data)
            with open(filename, "w") as f:
                json.dump(self.temp, f, indent=4)
            print("Booking added successfully.")
        else:
            print("Booking failed, please check the customer ID, room ID and availability.")

    @classmethod
    def cancel_booking(cls, cust_id, room_id):
        with open(filename, "r") as f:
            temp = json.load(f)
        for booking in temp["Booking"]:
            if booking["CustID"] == cust_id and booking["RoomID"] == room_id:
                temp["Booking"].remove(booking)
                with open(filename, "w") as f:
                    json.dump(temp, f, indent=4)
                print("Booking canceled successfully.")
                return
        print("Booking not found.")

    @classmethod
    def view_bookings(cls):
        with open(filename, "r") as f:
            temp = json.load(f)
        for booking in temp["Booking"]:
            customer_name = None
            room_type = None
            for customer in temp["Customers"]:
                if customer["ID"] == booking["CustID"]:
                    customer_name = customer["Name"]
                    break
            for room in temp["Rooms"]:
                if room["id"] == booking["RoomID"]:
                    room_type = room["Type"]
                    break
            print(f"Booking for customer {customer_name} in room type {room_type}")
            print(f"Arrival Date: {booking['ArrivalDate']}")

    @classmethod
    def BookedRoomsSpecificDate(cls, date):
        with open(filename, "r") as f:
            temp = json.load(f)
        for booking in temp["Booking"]:
            customer_name = None
            room_type = None
            if booking["ArrivalDate"] == date:
                for customer in temp["Customers"]:
                    if customer["ID"] == booking["CustID"]:
                        customer_name = customer["Name"]
                        break
                for room in temp["Rooms"]:
                    if room["id"] == booking["RoomID"]:
                        room_type = room["Type"]
                        break
                print(f"Booking for customer {customer_name} in room type {room_type}")
                print(f"Arrival Date: {booking['ArrivalDate']}")
            else:
                # except Exception as error:
                # print(f"Couldn't load the file - error {error}")
                print(f"there is no reservetions for {date}")

    @classmethod
    def AvailableroomsSpecificDate(cls, date):
        with open(filename, "r") as f:
            temp = json.load(f)
        available_rooms = []
        for room in temp["Rooms"]:
            room_id = room["id"]
            room_available = True
            for booking in temp["Booking"]:
                if booking["RoomID"] == room_id:
                    if (datetime.strptime(date, "%d/%m/%Y") >= datetime.strptime(booking["ArrivalDate"],
                                                                                          "%d/%m/%Y")) and (
                            datetime.strptime(date, "%d/%m/%Y") <= datetime.strptime(booking["DepartureDate"],
                                                                                              "%d/%m/%Y")):
                        room_available = False
                        break
            if room_available:
                available_rooms.append(room_id)
        print(len(available_rooms))


                # print(f"Arrival Date: {booking['ArrivalDate']}")
            # if count==0:
            #     # except Exception as error:
            #     # print(f"Couldn't load the file - error {error}")
            #     print(f"there is no Room Available for {date}")
            # print(f"there is {count} Available Rooms in {date}")

#
# book = Booking(10, 12, '20/10/2023', '25/10/2023')
# book.add_booking()
