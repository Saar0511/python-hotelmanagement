import json
from customers1 import Customers
filename = "./data/Customers.json"

def test_customers():
    # Test loading customers from file
    cust = Customers("John Doe", "123 Main St", "Anytown", "johndoe@example.com", 30)
    cust.load_customers()
    assert "Customers" in cust.temp
    assert len(cust.temp["Customers"]) > 0
    
    # Test adding a new customer
    cust = Customers("Jane Doe", "456 Park Ave", "Anycity", "janedoe@example.com", 25)
    cust.add_data()
    cust.load_customers()
    assert len(cust.temp["Customers"]) == len(cust.temp["Customers"])
    assert cust.temp["Customers"][-1]["Name"] == "Jane Doe"
    
    # Test viewing all customers
    cust.view_data()
    # Output should display all customer details
    
    # Test searching for a customer by name
    cust_name = input("Enter a customer name to search for: ")
    cust.Cust_by_name()
    # Output should display the details of the customer with the given name, if found
    
    # Test removing a customer
    cust_name = input("Enter a customer name to remove: ")
    cust.Remove_customer(cust_name)
    # Output should display 'Customer removed successfully' if the customer is found and removed, 
    # 'No customer found with the given name' otherwise.
   
test_customers()
