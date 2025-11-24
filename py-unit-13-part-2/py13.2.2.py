


#2. Simple Calculation using Method Overloading



class Calculation:
    def add(self, *args):
        return sum(args)

# --- Program Execution ---
calc = Calculation()

print("Sum of 2 numbers:", calc.add(10, 20))        #args 2
print("Sum of 3 numbers:", calc.add(10, 20, 30))      #args 3
print("Sum of 4 numbers:", calc.add(1, 2, 3, 4))     #args 4



class Demo:
    def show(self, *args, **kwargs):
        print("Positional arguments (args):", args)
        print("Keyword arguments (kwargs):", kwargs)

# --- Usage ---
d = Demo()

# Passing positional arguments
d.show(10, 20, 30)

# Passing keyword arguments
d.show(a=1, b=2, c=3)

# Passing both together
d.show(100, 200, x=5, y=10)
