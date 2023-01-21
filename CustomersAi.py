import tkinter as tk

from Booking import Booking
from Rooms import Rooms
from customers1 import Customers


class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.master.title("Almog and Saar Hotel")

    def create_widgets(self):
        self.add_room_button = tk.Button(self, text="1. Add a new room", command=self.add_room_popup)
        self.add_room_button.grid(row=0, column=0)

        self.add_customer_button = tk.Button(self, text="2. Add a new customer", command=self.add_customer_popup)
        self.add_customer_button.grid(row=1, column=0)

        self.book_room_button = tk.Button(self, text="3. Book a room", command=self.book_room_popup)
        self.book_room_button.grid(row=2, column=0)

        self.cancel_booking_button = tk.Button(self, text="4. Cancel booking", command=self.cancel_booking)
        self.cancel_booking_button.grid(row=3, column=0)

        self.display_rooms_button = tk.Button(self, text="5. Display all rooms", command=self.display_all_rooms_popup)
        self.display_rooms_button.grid(row=4, column=0)

        self.display_customers_button = tk.Button(self, text="6. Display all customers",
                                                  command=self.display_all_customers)
        self.display_customers_button.grid(row=5, column=0)

        self.display_bookings_button = tk.Button(self, text="7. Display all bookings",
                                                 command=self.display_all_bookings)
        self.display_bookings_button.grid(row=6, column=0)

        self.display_booked_rooms_button = tk.Button(self, text="8. Display booked rooms for a specific date",
                                                     command=self.display_booked_rooms)
        self.display_booked_rooms_button.grid(row=7, column=0)

        self.display_available_rooms_button = tk.Button(self, text="9. Display available rooms for a specific date",
                                                        command=self.display_available_rooms)
        self.display_available_rooms_button.grid(row=8, column=0)

        self.find_room_by_type_button = tk.Button(self, text="10. Find room by type", command=self.find_room_by_type)
        self.find_room_by_type_button.grid(row=9, column=0)

        self.find_room_by_number_button = tk.Button(self, text="11. Find room by number",
                                                    command=self.find_room_by_number)
        self.find_room_by_number_button.grid(row=9, column=0)
        self.find_customer_by_name_button = tk.Button(self, text="12. Find customer by name",
                                                      command=self.find_customer_by_name)
        self.find_customer_by_name_button.grid(row=10, column=0)

        self.remove_room_button = tk.Button(self, text="13. Remove room", command=self.remove_room)
        self.remove_room_button.grid(row=11, column=0)

        self.remove_customer_button = tk.Button(self, text="14. Remove customer", command=self.remove_customer)
        self.remove_customer_button.grid(row=12, column=0)

        self.exit_button = tk.Button(self, text="15. Exit", command=self.master.quit)
        self.exit_button.grid(row=13, column=0)

    def add_room_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Add a new room")

        room_type_label = tk.Label(popup, text="Room Type:")
        room_type_label.grid(row=0, column=0)

        room_type_var = tk.StringVar(popup)
        room_type_var.set("Basic")
        room_type_dropdown = tk.OptionMenu(popup, room_type_var, "Basic", "Deluxe", "Suite")
        room_type_dropdown.grid(row=0, column=1)

        add_button = tk.Button(popup, text="Add",
                               command=lambda: self.add_room(popup, room_type_var.get()))
        add_button.grid(row=5, column=1)

    def add_room(self, popup, room_type):
        if room_type == "Basic":
            size = "22mr"
            capacity = 10
            number_of_beds = 2
            price = 100
            Room = Rooms(size, capacity, number_of_beds, room_type, price)
            Room.Add_room()
            print("Room added.")
        elif room_type == "Deluxe":
            size = "26mr"
            capacity = 10
            number_of_beds = 2
            price = 200
            Room = Rooms(size, capacity, number_of_beds, room_type, price)
            Room.Add_room()
            print("Room added.")
        elif room_type == "Suite":
            size = "30mr"
            capacity = 10
            number_of_beds = 4
            price = 300
            Room = Rooms(size, capacity, number_of_beds, room_type, price)
            Room.Add_room()
            print("Room added.")
        popup.destroy()

    def add_customer_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Add a new Customer")

        Customer_type_label = tk.Label(popup, text="Add Customer Info:")
        Customer_type_label.grid(row=0, column=0)

        Customer_var = tk.StringVar(popup)

        Name_label = tk.Label(popup, text="Name:")
        Name_label.grid(row=1, column=0)

        Name_entry = tk.Entry(popup)
        Name_entry.grid(row=1, column=1)

        Address_label = tk.Label(popup, text="Address:")
        Address_label.grid(row=2, column=0)

        Address_entry = tk.Entry(popup)
        Address_entry.grid(row=2, column=1)

        City_label = tk.Label(popup, text="City:")
        City_label.grid(row=3, column=0)

        City_entry = tk.Entry(popup)
        City_entry.grid(row=3, column=1)

        Email_label = tk.Label(popup, text="Email:")
        Email_label.grid(row=4, column=0)

        Email_entry = tk.Entry(popup)
        Email_entry.grid(row=4, column=1)

        Age_label = tk.Label(popup, text="Age:")
        Age_label.grid(row=5, column=0)

        Age_entry = tk.Entry(popup)
        Age_entry.grid(row=5, column=1)
        print(Customer_var.get())
        add_button = tk.Button(popup, text="Add",
                               command=lambda: self.add_customer(popup, Name_entry.get(), Address_entry.get(),
                                                                 City_entry.get(), Email_entry.get(), Age_entry.get()))
        add_button.grid(row=6, column=1)

      # popup.destroy()

    def display_all_rooms_popup(self):
        popup = tk.Toplevel(self)
        popup.geometry("800x600")
        popup.title("All Rooms")

        rooms_list = Rooms.display_All_Rooms()

        listbox = tk.Listbox(popup,width=600,height=800)
        listbox.grid(row=0, column=0)



        listbox.insert(tk.END, rooms_list)



    def add_customer(self, popup, customer_name, customer_address, customer_city, customer_email, customer_age):
        Cust = Customers(customer_name, customer_address, customer_city, customer_email, customer_age)
        Cust.add_data()
        popup.destroy()


    def book_room_popup(self):
        pass

    def cancel_booking(self):
        pass

    def display_all_rooms(self):
        Rooms.display_All_Rooms()

    def display_all_customers(self):
        Customers.view_data()

    def display_all_bookings(self):
        Booking.View_All_Booking()

    def display_booked_rooms(self):
        pass

    def display_available_rooms(self):
        pass

    def find_room_by_type(self):
        pass

    def find_room_by_number(self):
        pass

    def find_customer_by_name(self):
        pass

    def remove_room(self):
        pass

    def remove_customer(self):
        pass


root = tk.Tk()
app = MainApplication(master=root)
app.mainloop()
