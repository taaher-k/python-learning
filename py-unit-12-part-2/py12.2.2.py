#Using encapsulation get the employee basic salary, bonus, loss of pay and
#calculate the total salary.







class EmployeeSalary:
    def __init__(self, basic_salary, bonus, loss_of_pay):
        # Private attributes (encapsulation)
        self.__basic_salary = basic_salary
        self.__bonus = bonus
        self.__loss_of_pay = loss_of_pay

    # Getter methods
    def get_basic_salary(self):
        return self.__basic_salary

    def get_bonus(self):
        return self.__bonus

    def get_loss_of_pay(self):
        return self.__loss_of_pay

    # Method to calculate total salary
    def calculate_total_salary(self):
        total = self.__basic_salary + self.__bonus - self.__loss_of_pay
        return total

    # Display method
    def display_salary_details(self):
        print("\n--- Salary Details ---")
        print(f"Basic Salary : Rs.{self.get_basic_salary()}")
        print(f"Bonus        : Rs.{self.get_bonus()}")
        print(f"Loss of Pay  : Rs.{self.get_loss_of_pay()}")
        print(f"Total Salary : Rs.{self.calculate_total_salary()}")



# --- Program Execution ---
emp1 = EmployeeSalary(30000, 5000, 2000)
emp1.display_salary_details()

emp2 = EmployeeSalary(50000, 6000, 3500)
emp1.display_salary_details()









class EmployeeSalary:
    def __init__(self, basic_salary, bonus, loss_of_pay):
        self.__basic_salary = basic_salary
        self.__bonus = bonus
        self.__loss_of_pay = loss_of_pay

    # Getter methods
    def get_basic_salary(self):
        return self.__basic_salary

    def get_bonus(self):
        return self.__bonus

    def get_loss_of_pay(self):
        return self.__loss_of_pay

    # Setter methods (controlled updates)
    def set_bonus(self, new_bonus):
        if new_bonus >= 0:
            self.__bonus = new_bonus
        else:
            print("Bonus cannot be negative!")

    def set_loss_of_pay(self, new_loss):
        if new_loss >= 0:
            self.__loss_of_pay = new_loss
        else:
            print("Loss of pay cannot be negative!")

    # Business logic method
    def calculate_total_salary(self):
        return self.__basic_salary + self.__bonus - self.__loss_of_pay

    # Manipulation method
    def apply_increment(self, percentage):
        """Increase basic salary by a percentage"""
        increment = self.__basic_salary * (percentage / 100)
        self.__basic_salary += increment

    # Display method
    def display_salary_details(self):
        print("\n--- Salary Details ---")
        print(f"Basic Salary : Rs.{self.get_basic_salary()}")
        print(f"Bonus        : Rs.{self.get_bonus()}")
        print(f"Loss of Pay  : Rs.{self.get_loss_of_pay()}")
        print(f"Total Salary : Rs.{self.calculate_total_salary()}")


# --- Program Execution ---
emp1 = EmployeeSalary(30000, 5000, 2000)
emp1.display_salary_details()

# Manipulate data inside the class
emp1.apply_increment(10)   # Increase salary by 10%
emp1.set_bonus(7000)       # Update bonus
emp1.set_loss_of_pay(1000) # Update loss of pay

print("\nAfter Updates:")
emp1.display_salary_details()
