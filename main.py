from food_item import FoodItem
from restaurant import Restaurant
from menu import Menu
from orders import Order
from users import Admin, Customer, Employee

babar_hotel = Restaurant("Babar Hotel")

def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    customer = Customer(name = name, email = email, phone = phone, address = address)

    while True:
        print(f"-----Welcome {customer.name}-----")
        print("1. View Menu")
        print("2. Add Item to Your Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customer.view_menu(babar_hotel)

        elif choice == 2:
            item_name = input("Enter Item Name : ")
            item_quantity = int(input("Enter Item Quantity : "))
            customer.add_to_cart(babar_hotel, item_name, item_quantity)

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break

        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your email : ")
    phone = input("Enter Your phone : ")
    address = input("Enter Your address : ")
    admin = Admin(name = name, email = email, phone = phone, address = address)

    while True:
        print(f"-----Welcome {admin.name}-----")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Items")
        print("4. View Employees")
        print("5. Remove Item")
        print("6. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int (input("Enter Item Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(babar_hotel, item)

        elif choice == 2:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            phone = input("Enter Your Phone : ")
            address = input("Enter Your Address : ")
            age = input("Enter Your Age : ")
            designation = input("Enter Your Designation : ")
            salary = input("Enter Your Salary : ")
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(babar_hotel, employee)

        elif choice == 3:
            admin.view_menu(babar_hotel)

        elif choice == 4:
            admin.view_employee(babar_hotel)

        elif choice == 5:
            item_name = input("Enter Item Name : ")
            admin.remove_item(babar_hotel, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")


while True:
    print("--------Welcome--------")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")