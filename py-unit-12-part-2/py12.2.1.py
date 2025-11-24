#1. Design python application to model Employee of an “ABC” organization.

#Consider types of employees as

#a. Manager

#b. Sales Person

#Perform the following

#a. Implement simple inheritance where Employee (employee ID, First Name, Last

#Name, Current salary) is super class.

#b. Consider Manager (number of stock options) and SalesPerson (number of sales,commission rate) 

#as subclasses.


# Superclass: Employee
class Employee:
    def __init__(self, employee_id, first_name, last_name, current_salary):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.current_salary = current_salary

    def display_employee_details(self):
        print("\n--- Employee Details ---")
        print(f"Employee ID   : {self.employee_id}")
        print(f"Name          : {self.first_name} {self.last_name}")
        print(f"Current Salary: Rs.{self.current_salary}")


# Subclass: Manager
class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, current_salary, stock_options):
        super().__init__(employee_id, first_name, last_name, current_salary)
        self.stock_options = stock_options

    def display_employee_details(self):
        super().display_employee_details()
        print(f"Stock Options : {self.stock_options}")


# Subclass: SalesPerson
class SalesPerson(Employee):
    def __init__(self, employee_id, first_name, last_name, current_salary, number_of_sales, commission_rate):
        super().__init__(employee_id, first_name, last_name, current_salary)
        self.number_of_sales = number_of_sales
        self.commission_rate = commission_rate

    def calculate_commission(self):
        return self.number_of_sales * self.commission_rate

    def display_employee_details(self):
        super().display_employee_details()
        print(f"Number of Sales : {self.number_of_sales}")
        print(f"Commission Rate : Rs.{self.commission_rate}")
        print(f"Total Commission: Rs.{self.calculate_commission()}")



# --- Program Execution ---
# Manager object
m1 = Manager(101, "Alice", "Johnson", 75000, 50)
print("\n--- Manager Details ---")
m1.display_employee_details()

# SalesPerson object
s1 = SalesPerson(102, "Bob", "Smith", 50000, 120, 250)
print("\n--- SalesPerson Details ---")
s1.display_employee_details()
