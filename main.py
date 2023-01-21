import re

import Rooms1
from customers1 import Customers
from Rooms1 import Room
import customers1

MailCheck = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
ageCheck = re.compile(r'\d{2}')


def start():
    print("""Hello,
Welcome To Almog Hotel.
Please Choose One Of Our Options:
1.book A Room
2.Cancel Booking
3.Manager Menu""")
    Type = int(input())
    if Type == 1:
        BookAroom()

    if Type == 2:
        pass
    if Type == 3:
        pass

def BookAroom():
    print("""Hello,
please Choose One Of Our Options:
1.Basic
2.Deluxe
3.Suite""")
    Type = int(input())
    if Type == 1:
        Type="Basic"
        size="22Mr"
        Capacity=10
        NumberOfBeds=2
        Price=100
        BasicRoom=Room(Type,size,Capacity,NumberOfBeds,Price)
        BasicRoom.interduction()
    elif Type == 2:
        Type = "Deluxe"
        size = "26Mr"
        Capacity = 10
        NumberOfBeds = 2
        Price = 200
        DeluxeRoom=Room(Type,size,Capacity,NumberOfBeds,Price)
        DeluxeRoom.interduction()
    elif Type == 3:
        Type = "Basic"
        size = "30Mr"
        Capacity = 10
        NumberOfBeds = 4
        Price = 300
        SuiteRoom=Room(Type,size,Capacity,NumberOfBeds,Price)
        SuiteRoom.interduction()

    Continue = int(input())
    if Continue == 1:
        print(f"""Great We Will Love To Host You in our {Type} Room
Please Fill Your Information Below""")
        pass
        Reservation(Type)

        #####Booking######
    if Continue == 2:
        print("""Do You Want To Check Our Other Rooms?
1.Yes
2.No""")
        Check = int(input())
        if Check == 1:
            start()
        if Check == 2:
            print("Good Bye")
            exit()
# def select_Time(room):
#     ArrivalDate = input("please enter your ArrivalDate like this:11/11/2023")
#     DepartureDate = input("please enter your DepartureDate like this:11/11/2023")
#     #book = Booking.Booking(ArrivalDate, DepartureDate, room)
#     #book.TotalDays1()
#     #book.TotalPrice()
#    # book.__str__()


#def price1():
 #  book = Booking.Booking('15/10/2023', '20/2/2023',)
   # book.TotalPrice()

def Reservation(Type):
    Name = input("please enter your Name")
    Address = input("please enter your Address")
    City = input("please enter your City")
    Email = input("please enter Your Email")
    if not re.fullmatch(MailCheck, Email):
        raise Exception("Invalid Email")
    Age = input("please enter your age")
    if not re.fullmatch(ageCheck, Age):
        raise Exception("Invalid Age")
    ID = id(Name)
    Custumer = customers1.Customers(Name, Address, City, Email, Age, ID)
    Custumer.add_data()
    Custumer.interduction()


def View_data():
    customers1.view_data()


start()
