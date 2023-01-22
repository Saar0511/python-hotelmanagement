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
        print(ArrivalDate)

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
        arrival_date = datetime.strptime(arrival_date, "%Y-%m-%d")
        departure_date = datetime.strptime(departure_date, "%Y-%m-%d")
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
        for booking in self.temp["Booking"]:
            if booking["RoomID"] == room_id and (
                    (arrival_date >= datetime.strptime(booking["ArrivalDate"],
                                                       "%Y-%m-%d") and arrival_date <= datetime.strptime(
                        booking["DepartureDate"], "%Y-%m-%d")) or (
                            departure_date >= datetime.strptime(booking["ArrivalDate"],
                                                                "%Y-%m-%d") and departure_date <= datetime.strptime(
                        booking["DepartureDate"], "%Y-%m-%d")) or (
                            arrival_date <= datetime.strptime(booking["ArrivalDate"],
                                                              "%Y-%m-%d") and departure_date >= datetime.strptime(
                        booking["DepartureDate"], "%Y-%m-%d"))
            ):
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
            arrival = datetime.strptime(self.ArrivalDate, "%Y-%m-%d")
            departure = datetime.strptime(self.DepartureDate, "%Y-%m-%d")
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
            return True
        else:
            print("Booking failed, please check the customer ID, room ID and availability.")
            return False

    @classmethod
    def cancel_booking(cls, cust_id):
        with open(filename, "r") as f:
            temp = json.load(f)

        booking_found = False
        for booking in temp["Booking"]:
            if booking["CustID"] == cust_id:
                temp["Booking"].remove(booking)
                booking_found = True
                break

        if booking_found:
            with open(filename, "w") as f:
                json.dump(temp, f, indent=4)
            print("Booking canceled successfully.")
            return True
        else:
            print("Booking not found.")
            return False

    @classmethod
    def view_bookings(cls):
        with open(filename, "r") as f:
            temp = json.load(f)
        bookings = []
        for Book in temp["Booking"]:
            CustID = Book["CustID"]
            RoomID = Book["RoomID"]
            ArrivalDate = Book["ArrivalDate"]
            DepartureDate = Book["DepartureDate"]
            TotalPrice = Book["TotalPrice"]
            bookings.append((CustID, RoomID, ArrivalDate, DepartureDate, TotalPrice))
        return bookings

    @classmethod
    def BookedRoomsSpecificDate(cls, date):
        with open(filename, "r") as f:
            temp = json.load(f)
        list = []
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
                list.append((customer_name, room_type, booking['ArrivalDate']))
                return list

            else:
                # except Exception as error:
                # print(f"Couldn't load the file - error {error}")
                print(f"there is no reservetions for {date}")
                return False

        #return list

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
                    if (datetime.strptime(date, "%Y-%m-%d") >= datetime.strptime(booking["ArrivalDate"],
                                                                                 "%Y-%m-%d")) and (
                            datetime.strptime(date, "%Y-%m-%d") <= datetime.strptime(booking["DepartureDate"],
                                                                                     "%Y-%m-%d")):
                        room_available = False
                        break
            if room_available:
                available_rooms.append(f"{room_id}")
        if not available_rooms:
            return False
        return available_rooms
        # print(len(available_rooms))

        # print(f"Arrival Date: {booking['ArrivalDate']}")
        # if count==0:
        #     # except Exception as error:
        #     # print(f"Couldn't load the file - error {error}")
        #     print(f"there is no Room Available for {date}")
        # print(f"there is {count} Available Rooms in {date}")

#
