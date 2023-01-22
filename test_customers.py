import json
from customers1 import Customers
filename = "./data/Customers.json"

def test_add_data():
    customer = Customers("John Doe", "123 Main St", "New York", "johndoe@email.com", 30)
    assert customer.add_data() == True
    customer_list = Customers.display_All_Customers()
    assert customer_list[-1][0] == "John Doe"
    assert customer_list[-1][1] == "123 Main St"
    assert customer_list[-1][2] == "New York"
    assert customer_list[-1][3] == "johndoe@email.com"
    assert customer_list[-1][4] == 30

def test_display_All_Customers():
    customer_list = Customers.display_All_Customers()
    for R in customer_list:
            name = R[0]
            Address = R[1]
            City = R[2]
            Email = R[3]
            Age = R[4]
            ID = R[5]
            print(f"Customer ID: {ID}")
            print(f"name Of The Customer is: {name}")
            print(f"Address Of The Customer is: {Address}")
            print(f"City Of The Customer Is: {City}")
            print(f"Email Of The Customer: {Email}")
            print(f"Age Of The Customer: {Age}\n\n\n")
            print("")
    assert len(customer_list) > 0


def test_Cust_by_name():
    cust_name = input("Enter a customer name to search for: ")
    Cust=Customers.Cust_by_name(cust_name)
    if Cust != False:
            for R in Cust:
                name = R[0]
                Address = R[1]
                City = R[2]
                Email = R[3]
                Age = R[4]
                ID= R[5]
                print(f"Customer ID Is: {ID}")
                print(f"Customer Name Is: {name}")
                print(f"Customer Address Is: {Address}")
                print(f"Customer City Is: {City}")
                print(f"Customer Email Is : {Email}")
                print(f"Customer Age Is: {Age}")
                print("")

    


def test_Remove_customer():
    cust_name = input("Enter a customer name to remove: ")
    if Customers.Remove_customer(cust_name):
        print(f"{cust_name} Removed Succesfully")
    else:
        print(f"there is no customer{cust_name}")

test_add_data()
test_display_All_Customers()
test_Cust_by_name()
test_Remove_customer()