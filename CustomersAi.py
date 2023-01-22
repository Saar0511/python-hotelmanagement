import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter import RIGHT
from tkinter import TOP
from tkinter import Y
from tkcalendar import Calendar
from BookingAi import Booking
from Rooms import Rooms
from customers1 import Customers


class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.master.title("Almog And Saar Hotel")

    def display_Available_Rooms_By_Date_pop_up(self):
        book_room = tk.Toplevel()
        book_room.title("Display Available Room By Date")
        book_room.geometry("300x400")
        book_room.config()
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("my.Treeview", background="white",
                        fieldbackground="white", foreground="black",
                        fieldforeground="black")
        arrival_calendar_label = tk.Label(book_room, font=("Arial", 12), text="Arrival Date:")
        arrival_calendar_label.pack()
        arrival_calendar = Calendar(book_room, font=("Arial", 12), selectmode='day', year=2023, month=3, day=1,style="my.Treeview")
        arrival_calendar.pack(fill="both", expand=False)
        book_button = tk.Button(book_room, font=("Arial", 12), text="Display",
                                command=lambda: self.display_Available_Rooms_By_Date(book_room,
                                                                                  str(arrival_calendar.selection_get())))
        book_button.pack()

    def display_Available_Rooms_By_Date(self, displayRoom, ArrivalDate):
        view_bookings_window = tk.Toplevel(self.master)
        view_bookings_window.title(f"All Booking That Available for{ArrivalDate}")
        view_bookings_window.geometry("300x600")
        view_bookings_window.config()

        Book = Booking.AvailableroomsSpecificDate((ArrivalDate))

        # Create a Listbox widget to hold the room information
        room_list = tk.Listbox(view_bookings_window, width=600, height=800)
        room_list.grid(row=4, column=3)
        room_list.config(justify=tk.CENTER)
        room_list.pack(side=TOP)
        # room_list.insert(tk.END, "")

        # Create a Scrollbar widget and connect it to the Listbox
        scrollbar = tk.Scrollbar(view_bookings_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=room_list.yview)
        room_list.config(yscrollcommand=scrollbar.set)
        if Book != False:
            for B in Book:
                Number_Of_Room = B


                room_list.insert(tk.END, f"Room {int(Number_Of_Room)} Available in {ArrivalDate}")
                room_list.insert(tk.END, "")
            displayRoom.destroy()
        else:
            room_list.insert(tk.END, f"there is no Room Available In :{ArrivalDate}")

    def display_Booked_Rooms_By_Date_pop_up(self):
        book_room = tk.Toplevel()
        book_room.title("Display Booked Room By Date")
        book_room.geometry("300x400")
        book_room.config()
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("my.Treeview", background="white",
                        fieldbackground="white", foreground="black",
                        fieldforeground="black")
        arrival_calendar_label = tk.Label(book_room, text="Arrival Date:")
        arrival_calendar_label.pack()
        arrival_calendar = Calendar(book_room, font=("Arial", 12), selectmode='day', year=2023, month=3, day=1,style="my.Treeview")
        arrival_calendar.pack(fill="both", expand=False)
        book_button = tk.Button(book_room, font=("Arial", 12), text="Display",
                                command=lambda: self.display_Booked_Rooms_By_Date(book_room,str(arrival_calendar.selection_get())))
        book_button.pack()

    def display_Booked_Rooms_By_Date(self,displayRoom,ArrivalDate):
        view_bookings_window = tk.Toplevel(self.master)
        view_bookings_window.title(f"All Booking for{ArrivalDate}")
        view_bookings_window.geometry("300x600")
        view_bookings_window.config()

        Book=Booking.BookedRoomsSpecificDate(str(ArrivalDate))

        # Create a Listbox widget to hold the room information
        room_list = tk.Listbox(view_bookings_window, width=600, height=800)
        room_list.grid(row=4, column=3)
        room_list.config(justify=tk.CENTER)
        room_list.pack(side=TOP)
        # room_list.insert(tk.END, "")

        # Create a Scrollbar widget and connect it to the Listbox
        scrollbar = tk.Scrollbar(view_bookings_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=room_list.yview)
        room_list.config(yscrollcommand=scrollbar.set)
        if Book != False:
            for B in Book:
                name = B[0]
                Type = B[1]
                ArrivalDate = B[2]

                room_list.insert(tk.END, f"Customer Name: {name}")
                room_list.insert(tk.END, f"Room Type Is: {Type}")
                room_list.insert(tk.END, f"ArrivalDate is: {ArrivalDate}")
                room_list.insert(tk.END, "")
            displayRoom.destroy()
        else:
            room_list.insert(tk.END, f"there is no reservetions for :{ArrivalDate}")


    def create_widgets(self):
        self.add_room_button = tk.Button(self, text="1. Add a new room", command=self.add_room_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.add_room_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_customer_button = tk.Button(self, text="2. Add a new customer", command=self.add_customer_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.add_customer_button.grid(row=1, column=0, padx=5, pady=5)

        self.book_room_button = tk.Button(self, text="3. Book a room", command=self.book_room_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.book_room_button.grid(row=2, column=0, padx=5, pady=5)

        self.cancel_booking_button = tk.Button(self, text="4. Cancel booking", command=self.cancel_booking_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.cancel_booking_button.grid(row=3, column=0, padx=5, pady=5)

        self.display_rooms_button = tk.Button(self, text="5. Display all rooms", command=self.display_all_rooms_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.display_rooms_button.grid(row=4, column=0, padx=5, pady=5)

        self.display_customers_button = tk.Button(self, text="6. Display all customers",
                                                  command=self.display_all_customers_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.display_customers_button.grid(row=5, column=0, padx=5, pady=5)

        self.display_bookings_button = tk.Button(self, text="7. Display all bookings",
                                                 command=self.display_all_bookings, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.display_bookings_button.grid(row=6, column=0, padx=5, pady=5)

        self.display_booked_rooms_button = tk.Button(self, text="8. Display booked rooms for a specific date",
                                                     command=self.display_Booked_Rooms_By_Date_pop_up, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.display_booked_rooms_button.grid(row=7, column=0, padx=5, pady=5)

        self.display_available_rooms_button = tk.Button(self, text="9. Display available rooms for a specific date",
                                                        command=self.display_Available_Rooms_By_Date_pop_up, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.display_available_rooms_button.grid(row=8, column=0, padx=5, pady=5)

        self.find_room_by_type_button = tk.Button(self, text="10. Find room by type", command=self.find_room_by_Type_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.find_room_by_type_button.grid(row=9, column=0, padx=5, pady=5)

        self.find_room_by_number_button = tk.Button(self, text="11. Find room by number",
                                                    command=self.find_room_by_number_popup, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.find_room_by_number_button.grid(row=10, column=0, padx=5, pady=5)
        self.find_customer_by_name_button = tk.Button(self, text="12. Find customer by name",
                                                      command=self.find_customer_by_name, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.find_customer_by_name_button.grid(row=11, column=0, padx=5, pady=5)

        self.remove_room_button = tk.Button(self, text="13. Remove room", command=self.remove_room, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.remove_room_button.grid(row=12, column=0, padx=5, pady=5)

        self.remove_customer_button = tk.Button(self, text="14. Remove customer", command=self.remove_customer, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.remove_customer_button.grid(row=13, column=0, padx=5, pady=5)

        self.exit_button = tk.Button(self, text="15. Exit", command=self.master.quit, bg='#34eb7a', fg='black', font=('Arial', 12, 'bold'))
        self.exit_button.grid(row=14, column=0, padx=5, pady=5)

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
            if Room.Add_room():
                messagebox.showinfo("Success", "Room Added Successfully!")
            else:
                messagebox.showinfo("Failed", "Room Dont Added!")
        elif room_type == "Deluxe":
            size = "26mr"
            capacity = 10
            number_of_beds = 2
            price = 200
            Room = Rooms(size, capacity, number_of_beds, room_type, price)
            if Room.Add_room():
                messagebox.showinfo("Success", "Room Added Successfully!")
            else:
                messagebox.showinfo("Failed", "Room Dont Added!")
        elif room_type == "Suite":
            size = "30mr"
            capacity = 10
            number_of_beds = 4
            price = 300
            Room = Rooms(size, capacity, number_of_beds, room_type, price)
            if Room.Add_room():
                messagebox.showinfo("Success", "Room Added Successfully!")
            else:
                messagebox.showinfo("Failed", "Room Dont Added!")
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

        add_button = tk.Button(popup, text="Add",
                               command=lambda: self.add_customer(popup, Name_entry.get(), Address_entry.get(),
                                                                 City_entry.get(), Email_entry.get(), Age_entry.get()))
        add_button.grid(row=6, column=1)

    # popup.destroy()

    def display_all_rooms_popup(self):
        view_bookings_window = tk.Toplevel(self.master)
        view_bookings_window.title("All Rooms")
        view_bookings_window.geometry("300x600")
        view_bookings_window.config(bg="white")

        Room = Rooms.display_All_Rooms()

        # Create a Listbox widget to hold the room information
        room_list = tk.Listbox(view_bookings_window, width=400, height=800)
        room_list.grid(row=4, column=3)
        room_list.config(justify=tk.CENTER)
        room_list.pack(side=TOP)
        # room_list.insert(tk.END, "")

        # Create a Scrollbar widget and connect it to the Listbox
        scrollbar = tk.Scrollbar(view_bookings_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=room_list.yview)
        room_list.config(yscrollcommand=scrollbar.set)

        for R in Room:
            ID = R[0]
            Size = R[1]
            Capacity = R[2]
            NumberOfBeds = R[3]
            Type = R[4]
            Price = R[5]
            room_list.insert(tk.END, f"Room Number: {ID}")
            room_list.insert(tk.END, f"Size Of The Room is: {Size}")
            room_list.insert(tk.END, f"Room type: {Type}")
            room_list.insert(tk.END, f"Capacity: {Capacity}")
            room_list.insert(tk.END, f"NumberOfBeds: {NumberOfBeds}")
            room_list.insert(tk.END, f"Price: {Price}\n\n\n")
            room_list.insert(tk.END, "")

    def add_customer(self, popup, customer_name, customer_address, customer_city, customer_email, customer_age):
        Cust = Customers(customer_name, customer_address, customer_city, customer_email, customer_age)
        if Cust.add_data():
            messagebox.showinfo("Success", "Customer Added Successfully!")
        else:
            messagebox.showinfo("Failed", "Customer not Added!")
        popup.destroy()

    def book_room_popup(self):
        book_room = tk.Toplevel()
        book_room.title("Book Room")
        book_room.geometry("300x700")
        book_room.config()
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("my.Treeview", background="white",
                        fieldbackground="white", foreground="black",
                        fieldforeground="black")
        arrival_calendar_label = tk.Label(book_room, text="From: ")
        arrival_calendar_label.pack()
        arrival_calendar = Calendar(book_room, font=("Arial", 12), selectmode='day', year=2022, month=1, day=1,style="my.Treeview")
        arrival_calendar.pack(fill="both", expand=True)
        departure_calendar_label = tk.Label(book_room, text="To: ")
        departure_calendar_label.pack()
        departure_calendar = Calendar(book_room, font=("Arial", 12), selectmode='day', year=2022, month=1, day=1,style="my.Treeview")
        departure_calendar.pack(fill="both", expand=True)

        customer_id_label = tk.Label(book_room, text="Enter customer id: ")
        customer_id_label.pack()
        customer_id_entry = tk.Entry(book_room)
        customer_id_entry.pack()

        room_id_label = tk.Label(book_room, text="Enter room id: ")
        room_id_label.pack()
        room_id_entry = tk.Entry(book_room)
        room_id_entry.pack()

        book_button = tk.Button(book_room, text="Book",
                                command=lambda: self.book_room(book_room, int(customer_id_entry.get()),
                                                               int(room_id_entry.get()),
                                                               str(arrival_calendar.selection_get()),
                                                               str(departure_calendar.selection_get())))
        book_button.pack()

    def book_room(self, book_room, Custid, RoomID, ArrivalDate, DepartureDate):
        Book = Booking(Custid, RoomID, ArrivalDate, DepartureDate)
        if Book.add_booking():
            messagebox.showinfo("Success", "Booking added successfully!")
        else:
            messagebox.showinfo("Failed", "Booking failed, please check the customer ID, room ID and availability.")

        book_room.destroy()

    def cancel_booking_popup(self):
        cancel_booking_window = tk.Toplevel()
        cancel_booking_window.title("Cancel Booking")
        cancel_booking_window.geometry("300x200")
        cancel_booking_window.config()

        booking_id_label = tk.Label(cancel_booking_window, text="Enter Customer id: ")
        booking_id_label.pack()
        booking_id_entry = tk.Entry(cancel_booking_window)
        booking_id_entry.pack()

        cancel_button = tk.Button(cancel_booking_window, text="Cancel Booking",
                                  command=lambda: self.cancel_booking(cancel_booking_window, booking_id_entry.get()))
        cancel_button.pack()

    def cancel_booking(self, cancel_booking_window, ID):
        ID = int(ID)
        if Booking.cancel_booking(ID):
            messagebox.showinfo("Success", "Cancel Booking Successfully!")
        else:
            messagebox.showinfo("Failed", "Booking not Exist!")
        cancel_booking_window.destroy()

    def display_all_customers_popup(self):
        view_bookings_window = tk.Toplevel(self.master)
        view_bookings_window.title("All Customers")
        view_bookings_window.geometry("300x600")
        view_bookings_window.config()

        Cust = Customers.display_All_Customers()

        # Create a Listbox widget to hold the room information
        room_list = tk.Listbox(view_bookings_window, width=600, height=800)
        room_list.grid(row=4, column=3)
        room_list.config(justify=tk.CENTER)
        room_list.pack(side=TOP)
        # room_list.insert(tk.END, "")

        # Create a Scrollbar widget and connect it to the Listbox
        scrollbar = tk.Scrollbar(view_bookings_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=room_list.yview)
        room_list.config(yscrollcommand=scrollbar.set)

        for R in Cust:
            name = R[0]
            Address = R[1]
            City = R[2]
            Email = R[3]
            Age = R[4]
            ID = R[5]
            room_list.insert(tk.END, f"Customer ID: {ID}")
            room_list.insert(tk.END, f"name Of The Customer is: {name}")
            room_list.insert(tk.END, f"Address Of The Customer is: {Address}")
            room_list.insert(tk.END, f"City Of The Customer Is: {City}")
            room_list.insert(tk.END, f"Email Of The Customer: {Email}")
            room_list.insert(tk.END, f"Age Of The Customer: {Age}\n\n\n")
            room_list.insert(tk.END, "")

    def display_all_bookings(self):
        view_bookings_window = tk.Toplevel(self.master)
        view_bookings_window.title("All Bookings")
        view_bookings_window.geometry("300x600")
        view_bookings_window.config(bg="white")

        Book = Booking.view_bookings()

        # Create a Listbox widget to hold the room information
        room_list = tk.Listbox(view_bookings_window, width=600, height=800)
        room_list.grid(row=4, column=3)
        room_list.config(justify=tk.CENTER)
        room_list.pack(side=TOP)
        # room_list.insert(tk.END, "")

        # Create a Scrollbar widget and connect it to the Listbox
        scrollbar = tk.Scrollbar(view_bookings_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=room_list.yview)
        room_list.config(yscrollcommand=scrollbar.set)

        for R in Book:
            CustID = R[0]
            RoomID = R[1]
            ArrivalDate = R[2]
            DepartureDate = R[3]
            TotalPrice = R[4]
            room_list.insert(tk.END, f"Customer ID Is: {CustID}")
            room_list.insert(tk.END, f"Room Number Is: {RoomID}")
            room_list.insert(tk.END, f"ArrivalDate Is: {ArrivalDate}")
            room_list.insert(tk.END, f"DepartureDate Is : {DepartureDate}")
            room_list.insert(tk.END, f"TotalPrice Is: {TotalPrice}")
            room_list.insert(tk.END, "")

    def find_room_by_number_popup(self):
        find_room_by_number_window = tk.Toplevel()
        find_room_by_number_window.title("Find Room by Number")
        find_room_by_number_window.geometry("300x200")
        find_room_by_number_window.config()

        room_number_label = tk.Label(find_room_by_number_window, text="Enter Room Number: ")
        room_number_label.pack()
        room_number_entry = tk.Entry(find_room_by_number_window)
        room_number_entry.pack()

        find_button = tk.Button(find_room_by_number_window, text="Find Room",
                                command=lambda: self.find_room_by_number(find_room_by_number_window,
                                                                         room_number_entry.get()))
        find_button.pack()

    def find_room_by_Type_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Add a new room")

        room_type_label = tk.Label(popup, text="Room Type:")
        room_type_label.grid(row=0, column=0)
        popup.geometry("200x50")
        room_type_var = tk.StringVar(popup)
        room_type_var.set("Basic")
        room_type_dropdown = tk.OptionMenu(popup, room_type_var, "Basic", "Deluxe", "Suite")
        room_type_dropdown.grid(row=0, column=1)

        add_button = tk.Button(popup, text="Find",
                               command=lambda: self.find_room_by_Type(popup, room_type_var.get()))
        add_button.grid(row=5, column=1)
        # find_room_by_number_window = tk.Toplevel()
        # find_room_by_number_window.title("Find Room by Type")
        # find_room_by_number_window.geometry("300x200")
        # find_room_by_number_window.config()
        #
        # room_number_label = tk.Label(find_room_by_number_window, text="Enter Room Type: ")
        # room_number_label.pack()
        # room_number_entry = tk.Entry(find_room_by_number_window)
        # room_number_entry.pack()
        #
        # find_button = tk.Button(find_room_by_number_window, text="Find Room",
        #                         command=lambda: self.find_room_by_Type(find_room_by_number_window,
        #                                                                  room_number_entry.get()))
        # find_button.pack()

    def find_room_by_Type(self,find_room_by_number_window,room_Type):
        view_bookings_window = tk.Toplevel(self.master)
        view_bookings_window.title("Customer By Name")
        view_bookings_window.geometry("300x600")
        view_bookings_window.config(bg="white")

        Room = Rooms.RoomByType(str(room_Type))

        # Create a Listbox widget to hold the room information
        room_list = tk.Listbox(view_bookings_window, width=600, height=800)
        room_list.grid(row=4, column=3)
        room_list.config(justify=tk.CENTER)
        room_list.pack(side=TOP)
        # room_list.insert(tk.END, "")

        # Create a Scrollbar widget and connect it to the Listbox
        scrollbar = tk.Scrollbar(view_bookings_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=room_list.yview)
        room_list.config(yscrollcommand=scrollbar.set)
        if Room != False:
            for R in Room:
                ID = R[0]
                Size = R[1]
                Capacity = R[2]
                NumberOfBeds = R[3]
                Type = R[4]
                Price = R[5]
                room_list.insert(tk.END, f"Room Number Is: {ID}")
                room_list.insert(tk.END, f"Room Size Is: {Size}")
                room_list.insert(tk.END, f"Room Capacity Is: {Capacity}")
                room_list.insert(tk.END, f"Room NumberOfBeds Is: {NumberOfBeds}")
                room_list.insert(tk.END, f"Room Type Is : {Type}")
                room_list.insert(tk.END, f"Room Price Is: {Price}")
                room_list.insert(tk.END, "")

        else:
            room_list.insert(tk.END, f"Room Not Exist!")













    def find_room_by_number(self, find_room_by_number_window, room_number):
        room = Rooms.RoomByNumber(room_number)
        if room != "Room not found":
            display_window = tk.Toplevel()
            display_window.title("Customer Information")
            display_window.geometry("300x200")
            display_window.config()

            name_label = tk.Label(display_window, text=f"Size: {room.Size}")
            name_label.pack()
            address_label = tk.Label(display_window, text=f"Capacity: {room.Capacity}")
            address_label.pack()
            city_label = tk.Label(display_window, text=f"NumberOfBeds: {room.NumberOfBeds}")
            city_label.pack()
            email_label = tk.Label(display_window, text=f"Type: {room.Type}")
            email_label.pack()
            age_label = tk.Label(display_window, text=f"Price: {room.Price}")
            age_label.pack()

            close_button = tk.Button(display_window, text="Close", command=display_window.destroy)
            close_button.pack()

    def find_customer_by_name(self):

        find_name_window = tk.Toplevel()
        find_name_window.title("Find customer by name")
        find_name_window.geometry("300x200")
        find_name_window.config()

        name_label = tk.Label(find_name_window, text="Enter customer name: ")
        name_label.pack()
        name_entry = tk.Entry(find_name_window)
        name_entry.pack()

        find_button = tk.Button(find_name_window, text="Find",
                                command=lambda: self.display_customer_by_name(find_name_window, name_entry.get()))
        find_button.pack()

    def display_customer_by_name(self, find_name_window, name):
        view_bookings_window = tk.Toplevel(self.master)
        view_bookings_window.title("Customer By Name")
        view_bookings_window.geometry("300x600")
        view_bookings_window.config(bg="white")

        Book = Customers.Cust_by_name(str(name))

        # Create a Listbox widget to hold the room information
        room_list = tk.Listbox(view_bookings_window, width=600, height=800)
        room_list.grid(row=4, column=3)
        room_list.config(justify=tk.CENTER)
        room_list.pack(side=TOP)
        # room_list.insert(tk.END, "")

        # Create a Scrollbar widget and connect it to the Listbox
        scrollbar = tk.Scrollbar(view_bookings_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=room_list.yview)
        room_list.config(yscrollcommand=scrollbar.set)
        if Book != False:
            for R in Book:
                name = R[0]
                Address = R[1]
                City = R[2]
                Email = R[3]
                Age = R[4]
                ID= R[5]
                room_list.insert(tk.END, f"Customer ID Is: {ID}")
                room_list.insert(tk.END, f"Customer Name Is: {name}")
                room_list.insert(tk.END, f"Customer Address Is: {Address}")
                room_list.insert(tk.END, f"Customer City Is: {City}")
                room_list.insert(tk.END, f"Customer Email Is : {Email}")
                room_list.insert(tk.END, f"Customer Age Is: {Age}")
                room_list.insert(tk.END, "")

        else:
            room_list.insert(tk.END, f"Customer Not Exist!")






        # customer = Customers.Cust_by_name(name)
        # if customer != "Customer not found":
        #     display_window = tk.Toplevel()
        #     display_window.title("Customer Information")
        #     display_window.geometry("300x200")
        #     display_window.config()
        #
        #     name_label = tk.Label(display_window, text=f"Name: {customer.Name}")
        #     name_label.pack()
        #     address_label = tk.Label(display_window, text=f"Address: {customer.Address}")
        #     address_label.pack()
        #     city_label = tk.Label(display_window, text=f"City: {customer.City}")
        #     city_label.pack()
        #     email_label = tk.Label(display_window, text=f"Email: {customer.Email}")
        #     email_label.pack()
        #     age_label = tk.Label(display_window, text=f"Age: {customer.Age}")
        #     age_label.pack()
        #
        #     close_button = tk.Button(display_window, text="Close", command=display_window.destroy)
        #     close_button.pack()
        #
        # else:
        #     messagebox.showinfo("Info", "Customer not found")
        # find_name_window.destroy()

    def remove_room(self):
        remove_room_window = tk.Toplevel(self.master)
        remove_room_window.title("Remove Room")
        remove_room_window.geometry("400x200")
        remove_room_window.config()

        room_number_label = tk.Label(remove_room_window, text="Enter Room Number:")
        room_number_label.pack()
        room_number_entry = tk.Entry(remove_room_window)
        room_number_entry.pack()
        Remove = tk.Button(remove_room_window, text="Remove",
                           command=lambda: self.remove_roomm(room_number_entry.get(), remove_room_window))
        Remove.pack()

    def remove_roomm(self, number, remove_room_window):
        # Rooms.Remove_Room(int(number))
        if Rooms.Remove_Room(int(number)):
            messagebox.showinfo("Success", "Room Removed Successfully!")
        else:
            messagebox.showinfo("Failed", "Room not Exist!")
        remove_room_window.destroy()

    def remove_customer(self):
        remove_room_window = tk.Toplevel(self.master)
        remove_room_window.title("Remove Customer")
        remove_room_window.geometry("400x200")
        remove_room_window.config()

        Name_label = tk.Label(remove_room_window, text="Enter Customer Name:")
        Name_label.pack()
        Name_entry = tk.Entry(remove_room_window)
        Name_entry.pack()
        Remove = tk.Button(remove_room_window, text="Remove",
                           command=lambda: self.remove_Customerr(Name_entry.get(), remove_room_window))
        Remove.pack()

    def remove_Customerr(self, Name, remove_room_window):
        # Rooms.Remove_Room(int(number))
        if Customers.Remove_customer(Name):
            messagebox.showinfo("Sucess", "Customer Removed Successfully!")
        else:
            messagebox.showinfo("Failed", "Customer not Exist!")
        remove_room_window.destroy()


root = tk.Tk()
app = MainApplication(master=root)
app.mainloop()
