#2. Create a Temperature class. Make two methods :
#1. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.






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
