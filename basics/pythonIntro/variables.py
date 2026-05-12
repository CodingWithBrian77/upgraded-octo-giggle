# Variable = A container for a value(string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# String
first_name = "Brian"
food = "fried chicken"
email = "brian123@fake.com"

# Prints Brian
print(first_name)

# Using Formatted string (f-string) prints Hello Brian
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integer (Whole numbers) NO QUOTES
age = 20
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} km")

# Boolean (True or False, T/F must be cap)
is_student = True
for_sale = True

# booleans are typically handled internally instead of printing directly

print(f"Are you a student?: {is_student}")
print(f"Is this item for sale?: {for_sale}")





