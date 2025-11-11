#Create a module as circle.py. Define function to find area and perimeter.
#Write a main program to read radius as user input and call the functions.

#1
"""
# circle.py

import math

def area(radius):
   # Returns the area of a circle given the radius.
    return math.pi * radius ** 2

def perimeter(radius):
    # Returns the perimeter (circumference) of a circle given the radius.
    return 2 * math.pi * radius
"""

#2

# main.py

import circle

# Read radius from user
radius = float(input("Enter the radius of the circle: "))

# Call functions from circle module
circle_area = circle.area(radius)
circle_perimeter = circle.perimeter(radius)

# Display results
print(f"Area of the circle: {circle_area:.2f}")
print(f"Perimeter of the circle: {circle_perimeter:.2f}")



#3

pi = 3.14159


def area(radius):
    return pi * radius * radius

def perimeter(radius):
    return 2 *  pi * radius



f = float(input("enter the radius of the circle"))


circl_area = area(f)
circle_perimeter = perimeter(f)

print(circl_area,circle_perimeter)

