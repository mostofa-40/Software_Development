from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if not item:
            print("Item not found")
            return

        already_in_cart = self.cart.items.get(item, 0)
        if quantity + already_in_cart > item.quantity:
            print("Requested quantity exceeds available stock")
        else:
            self.cart.add_item(item, quantity)
            print("Item added to cart")

    def view_cart(self):
        print("--------Cart--------")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")

    def pay_bill(self):
        if not self.cart.items:
            print("Cart is empty")
            return

        for item, quantity in self.cart.items.items():
            item.quantity -= quantity

        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()