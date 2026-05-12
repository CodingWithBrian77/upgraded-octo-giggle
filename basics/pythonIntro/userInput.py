# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# allows user to input data, doesn't actually do anything though
# input("What is your name?")

# gives name variable value user inputs
name = input("What is your name?: ")
# you can typecast off the jump instead of doing it later
age = int(input("How old are you?: "))

#generates TypeError, as age is a string, must be converted into integer
#age = age + 1

#typecast inorder to do arithmetic
#age = int(age)
#age = age + 1

# prints corresponding statement with userinput in place of the variables
print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old!")

