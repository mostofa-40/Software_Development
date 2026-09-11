from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("--------Employee List--------")
        for employee in self.employees:
            print(employee.name, employee.email, employee.phone, employee.address)