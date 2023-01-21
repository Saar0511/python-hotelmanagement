from Rooms import Rooms
from customers1 import Customers
from BookingAi import Booking

# from  import Booking

def main():
    # filedata = Rooms.load_rooms("./data/Rooms.json")
    # customers = Customers.load_customers_from_file("customers.json")
    # bookings = Customers.load_bookings_from_file("bookings.json")
    while True:
        print("1. Add a new room")
        print("2. Add a new customer")
        print("3. Book a room")
        print("4. Cancel booking")
        print("5. Display all rooms")
        print("6. Display all customers")
        print("7. Display all bookings")
        print("8. Display booked rooms for a specific date")
        print("9. Display available rooms for a specific date")
        print("10. Find room by type")
        print("11. Find room by number")
        print("12. Find customer by name")
        print("13. Remove room")
        print("14. Remove customer")
        print("15. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            choice1 = input("Enter room type \n1 for Basic\n2 for Deluxe\n3 for Suite:\n ")
            if choice1 == "1":
                room_type = "Basic"
                size = "22mr"
                capacity = 10
                number_of_beds = 2
                price = 100
                Room = Rooms(size, capacity, number_of_beds, room_type, price)
                Room.Add_room()
                print("Room added.")
            elif choice1 == "2":
                size = "26mr"
                capacity = 10
                number_of_beds = 2
                room_type = "Deluxe"
                price = 200
                Room = Rooms(size, capacity, number_of_beds, room_type, price)
                Room.Add_room()
                print("Room added.")
            elif choice1 == "3":
                size = "30mr"
                capacity = 10
                number_of_beds = 4
                room_type = "Suite"
                price = 300
                Room = Rooms(size, capacity, number_of_beds, room_type, price)
                Room.Add_room()
                print("Room added.")
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            customer_address = input("Enter customer address: ")
            customer_city = input("Enter customer city: ")
            customer_email = input("Enter customer email: ")
            customer_age = input("Enter customer age: ")

            Cust = Customers(customer_name, customer_address, customer_city, customer_email, customer_age)
            Cust.add_data()
            print("Customer added.")
        elif choice == "3":
            customer_id = int(input("Enter customer id: "))
            room_id = int(input("Enter room id: "))
            arrival_date = str(input("Enter arrival date (YYYY-MM-DD): "))
            departure_date = str(input("Enter departure date (YYYY-MM-DD): "))
            Book=Booking(customer_id,room_id,arrival_date,departure_date)
            Book.add_booking()



            # Book=Booking(bookings, customer_id, room_id, arrival_date, departure_date, total_price)

        elif choice == "4":
            customer_id = int(input("Enter customer id: "))
            room_id = int(input("Enter room id: "))
            booking=Booking()
            booking.cancel_booking(customer_id,room_id)
            #booking_id = input("Enter booking id: ")
            #Bookings
            pass

        elif choice == "5":
            Rooms.display_All_Rooms()
        elif choice == "6":
            Customers.view_data()
        elif choice == "7":
            Booking.view_bookings()

            # Booking.display_all_bookings(bookings)
        elif choice == "8":
            date = input("Enter date (YYYY-MM-DD): ")
            Booking.BookedRoomsSpecificDate(date)
        elif choice == "9":
            date = input("Enter date (YYYY-MM-DD): ")
            Booking.AvailableroomsSpecificDate(date)
        # Room.display_available_rooms_for_date(rooms, bookings, date)
        elif choice == "10":

            room=Rooms.RoomByType()
        elif choice == "11":
            room=Rooms.RoomByNumber()
        elif choice == "12":
            cust=Customers.Cust_by_name()
            pass
            # customer_name = input
        elif choice == "13":
            print(Rooms.Remove_Room())
        elif choice == "14":
            print(Customers.Remove_customer())

main()
