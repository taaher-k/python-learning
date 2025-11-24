

#Write a program using Hierarchical Inheritance.    






# Base class
class Employee:
    def __init__(self, emp_id, first_name, last_name, salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary}")

# Subclass 1
class Manager(Employee):
    def __init__(self, emp_id, first_name, last_name, salary, stock_options):
        super().__init__(emp_id, first_name, last_name, salary)
        self.stock_options = stock_options

    def display_info(self):
        super().display_info()
        print(f"Stock Options: {self.stock_options}")

# Subclass 2
class SalesPerson(Employee):
    def __init__(self, emp_id, first_name, last_name, salary, sales, commission_rate):
        super().__init__(emp_id, first_name, last_name, salary)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_commission(self):
        return self.sales * self.commission_rate

    def display_info(self):
        super().display_info()
        print(f"Sales: {self.sales}, Commission Rate: {self.commission_rate}, "
              f"Total Commission: {self.calculate_commission()}")

# --- Usage ---
m1 = Manager(101, "Alice", "Johnson", 80000, 50)
s1 = SalesPerson(102, "Bob", "Smith", 50000, 200, 0.05)

print("Manager Details:")
m1.display_info()

print("\nSalesPerson Details:")
s1.display_info()
