#Create class Employee with name, Id, designation,

#department as members. Also create separate class for Salary. Properties

#in salary class are basic pay, hra , pf , insurance. Write methods to read


#values for all properties and separate method to display that.





class Employee:
    def __init__(self, name, emp_id, designation, department):
        # Initialize employee details
        self.name = name
        self.emp_id = emp_id
        self.designation = designation
        self.department = department

    def display_employee(self):
        print("\n--- Employee Details ---")
        print(f"Name        : {self.name}")
        print(f"ID          : {self.emp_id}")
        print(f"Designation : {self.designation}")
        print(f"Department  : {self.department}")


class Salary:
    def __init__(self):
        # Initialize salary properties
        self.basic_pay = 0
        self.hra = 0
        self.pf = 0
        self.insurance = 0

    # Method to read values
    def read_values(self):
        self.basic_pay = float(input("Enter Basic Pay: "))
        self.hra = float(input("Enter HRA: "))
        self.pf = float(input("Enter PF: "))
        self.insurance = float(input("Enter Insurance: "))

    # Method to display values
    def display(self):
        print("\n--- Salary Details ---")
        print(f"Basic Pay   : Rs.{self.basic_pay}")
        print(f"HRA         : Rs.{self.hra}")
        print(f"PF          : Rs.{self.pf}")
        print(f"Insurance   : Rs.{self.insurance}")





# --- Program Execution ---
# Create Employee object
emp1 = Employee("Alice", 101, "Software Engineer", "IT")
emp1.display_employee()

# Create Salary object
sal1 = Salary()
sal1.read_values()
sal1.display()


