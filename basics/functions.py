# function = A block of reusable code
#            place () after the function name to invoke it
# return   = statement used to end a function
#            and send a result back to the caller

# function with no parameters
def happy_birthday1():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday1()

# function with 1 parameter
def happy_birthday2(name):
    print(f"Happy birthday to {name}!")
    print(f"You are old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday2("Brian")
happy_birthday2("Steve")
happy_birthday2("Joe")

# function with 2 parameters, order must match invoking argument
def happy_birthday3(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday3("Brian", 20) # invoke argument order must match function parameters
happy_birthday3("Steve", 30)
happy_birthday3("Joe", 40)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("CodingWithBrian77", 100.01, "01/01/2026")

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("joe", "smith")
print(full_name)
