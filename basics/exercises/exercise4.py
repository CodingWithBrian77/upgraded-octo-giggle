import math

# Exercise 4 displays the area of a circle with user inputted values
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)

#displays area but with huge decimal numbers
print(f"The area of the circle is: {area}cm²")
print(f"The rounded area of the circle is: {round(area, 2)}cm²")
