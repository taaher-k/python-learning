#Write a class with constructor. Initialize 2 numbers in constructor. Write
#methods to return quotient(both division and floor division) and reminder
#of those 2 numbers.


class DivisionOperations:
    def __init__(self, num1, num2):
        # Initialize two numbers
        self.num1 = num1
        self.num2 = num2

    # Method to return quotient (true division)
    def get_division(self):
        if self.num2 == 0:
            return "Division by zero not allowed"
        return self.num1 / self.num2

    # Method to return quotient (floor division)
    def get_floor_division(self):
        if self.num2 == 0:
            return "Division by zero not allowed"
        return self.num1 // self.num2

    # Method to return remainder
    def get_remainder(self):
        if self.num2 == 0:
            return "Division by zero not allowed"
        return self.num1 % self.num2



# --- Program Execution ---
obj = DivisionOperations(17, 5)

print("Division Quotient:", obj.get_division())       # 17 / 5 = 3.4
print("Floor Division Quotient:", obj.get_floor_division())  # 17 // 5 = 3
print("Remainder:", obj.get_remainder())             # 17 % 5 = 2
