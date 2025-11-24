




from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def salary(self):
        """Calculate salary for the employee"""
        pass

    @abstractmethod
    def attendance(self):
        """Return attendance details"""
        pass


# Derived Class 1: Marketing Employee
class MarketingEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, bonus):
        super().__init__(emp_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def salary(self):
        return self.base_salary + self.bonus

    def attendance(self):
        return "Full-time, 5 days a week"


# Derived Class 2: Part-Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def salary(self):
        return self.hourly_rate * self.hours_worked

    def attendance(self):
        return f"Part-time, {self.hours_worked} hours per week"


# --- Program Execution ---
m_emp = MarketingEmployee(101, "Alice", 50000, 10000)
p_emp = PartTimeEmployee(102, "Bob", 500, 20)

print("Marketing Employee:")
print(f"Name: {m_emp.name}, Salary: {m_emp.salary()}, Attendance: {m_emp.attendance()}")

print("\nPart-Time Employee:")
print(f"Name: {p_emp.name}, Salary: {p_emp.salary()}, Attendance: {p_emp.attendance()}")
