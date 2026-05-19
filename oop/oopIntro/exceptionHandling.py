# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError, etc.)
#             1. try, 2. except, 3. finally

# 1 / 0 # ZeroDivisionError
# 1 + "1" # TypeError
# int("pizza") # ValueError

try:
    number = int(input("Enter a number: "))
    print(1 / number) # if user types in 0 or a string, you get error(s)
except ZeroDivisionError: # if a user attempts to divide by 0...
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally: # always executes last, regardless if there is an exception or not
    print("Do some cleanup here")
    