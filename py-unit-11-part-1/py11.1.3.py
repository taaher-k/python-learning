#Create a class Employee with methods to assign data and print data.


#1

"""
class employees:
    def __init__(self,name,role,salary):
        self.name= name
        self.role= role
        self.salary = salary

    def showdata(self):
        
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        

    
name = input("enter your name ")

role = input("enter your role ")

salary = input("enter your salary ")

na= employees(name,role,salary)
na.showdata()









"""

"""
class Employee:
    def __init__(self):
        # Initialize attributes with default values
        self.name = ""
        self.emp_id = 0
        self.department = ""
        self.salary = 0.0

    # Method to assign data
    def assignData(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    # Method to print data
    def printData(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Department:", self.department)
        print("Salary:", self.salary)


# --- Program Execution ---
emp1 = Employee()
emp1.assignData("Taaher", 101, "Software Development", 45000)
emp1.printData()









#3


#Hybrid Employee Class


class Employee:
    def __init__(self, name="", role="", salary=0.0):
        # Constructor initializes attributes (can be empty or with values)
        self.name = name
        self.role = role
        self.salary = salary

    # Method to assign or update data later
    def assignData(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    # Method to print employee details
    def showData(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        

# --- Program Execution ---

# Option 1: Initialize with constructor
emp1 = Employee("Taaher", "Developer", 45000)
emp1.showData()

# Option 2: Create empty object, assign later
emp2 = Employee()
emp2.assignData("Ali", "Tester", 30000)
emp2.showData()

"""



#4

import pandas as pd

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def showData(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print("-" * 30)


# --- Program Execution ---
# Read Excel file
df = pd.read_excel("employees.xlsx")   # requires openpyxl installed

# Create Employee objects for each row
employees_list = []
for index, row in df.iterrows():
    emp = Employee(row["Name"], row["Role"], row["Salary"])
    employees_list.append(emp)

# Print all employee data
for emp in employees_list:
    emp.showData()
