#2. Create a Temperature class. Make two methods :
#1. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.




class Temperature:
    def __init__(self, value, scale="C"):
        # value = numeric temperature
        # scale = "C" for Celsius or "F" for Fahrenheit
        self.value = value
        self.scale = scale.upper()

    def convertFahrenheit(self):
        if self.scale == "C":
            fahrenheit = (self.value * 9/5) + 32
            print(f"{self.value}°C = {fahrenheit:.2f}°F")
        else:
            print("Temperature is already in Fahrenheit.")

    def convertCelsius(self):
        if self.scale == "F":
            celsius = (self.value - 32) * 5/9
            print(f"{self.value}°F = {celsius:.2f}°C")
        else:
            print("Temperature is already in Celsius.")


# Example usage:
# Initialize with Celsius
temp1 = Temperature(25, "C")
temp1.convertFahrenheit()

# Initialize with Fahrenheit
temp2 = Temperature(77, "F")
temp2.convertCelsius()







class Temperature:
    # Method to convert Celsius to Fahrenheit
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")

    # Method to convert Fahrenheit to Celsius
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")


# --- Program Execution ---
t = Temperature()

# Example conversions
c = float(input("Enter temperature in Celsius: "))
t.convertFahrenheit(c)

f = float(input("Enter temperature in Fahrenheit: "))
t.convertCelsius(f)





#2


#WITH CONSTRUCTOR

class Temperature:
    def __init__(self, value):   # constructor
        self.value = value       # initialize temperature value

    def convertFahrenheit(self):
        fahrenheit = (self.value * 9/5) + 32
        print(f"{self.value}°C = {fahrenheit}°F")

    def convertCelsius(self):
        celsius = (self.value - 32) * 5/9
        print(f"{self.value}°F = {celsius}°C")


# --- Program Execution ---
# Convert Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
temp1 = Temperature(c)          # constructor initializes with Celsius
temp1.convertFahrenheit()

# Convert Fahrenheit to Celsius
f = float(input("Enter temperature in Fahrenheit: "))
temp2 = Temperature(f)          # constructor initializes with Fahrenheit
temp2.convertCelsius()
