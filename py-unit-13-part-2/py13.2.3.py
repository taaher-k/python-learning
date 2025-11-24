#Create a base class Employee and get staff id, name, basic, salary, loss of
#pay from the user. Create a sub class Trainee extends Employee and get
#incentives and calculate net pay print it using method overriding.



class Employee:

    def __init__(self, staff_id, name, basic_salary, loss_of_pay):
        self.staff_id = staff_id
        self.name = name
        self.basic_salary = basic_salary
        self.loss_of_pay = loss_of_pay

    def calculate_salary(self):
        # Salary after deducting loss of pay
        return self.basic_salary - self.loss_of_pay

    def display_details(self):
        print("\n--- Employee Details ---")
        print(f"Staff ID     : {self.staff_id}")
        print(f"Name         : {self.name}")
        print(f"Basic Salary : Rs.{self.basic_salary}")
        print(f"Loss of Pay  : Rs.{self.loss_of_pay}")
        print(f"Net Salary   : Rs.{self.calculate_salary()}")


# Subclass Trainee
class Trainee(Employee):
    def __init__(self, staff_id, name, basic_salary, loss_of_pay, incentives):
        super().__init__(staff_id, name, basic_salary, loss_of_pay)
        self.incentives = incentives

    # Method overriding
    def calculate_salary(self):
        # Net pay includes incentives
        return (self.basic_salary - self.loss_of_pay) + self.incentives

    def display_details(self):
        print("\n--- Trainee Details ---")
        print(f"Staff ID     : {self.staff_id}")
        print(f"Name         : {self.name}")
        print(f"Basic Salary : Rs.{self.basic_salary}")
        print(f"Loss of Pay  : Rs.{self.loss_of_pay}")
        print(f"Incentives   : Rs.{self.incentives}")
        print(f"Net Salary   : Rs.{self.calculate_salary()}")


# --- Program Execution ---
# Base Employee
emp = Employee(101, "Alice", 30000, 2000)
emp.display_details()

# Trainee Employee
trainee = Trainee(102, "Bob", 20000, 1000, 3000)
trainee.display_details()


