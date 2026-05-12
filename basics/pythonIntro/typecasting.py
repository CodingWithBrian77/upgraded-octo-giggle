# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Brian Spaulding"
age = 20
gpa = 3.5
is_student = True

# nothing displays
type(name)
# prints data type of variable
print(type(name))

# 3.5 now becomes 3 due to truncating
gpa = int(gpa)
# prints 3 as gpa is now an int
print(gpa)

# 20 now becomes 20.0
age = float(age)
# prints 20.0 instead of 20.0 as age is now a float
print(age)

# 20.0 is still 20.0, just in string form, cannot add/subtract etc now
age = str(age)
# prints 20.0
print(age)
# shows type as string
print(type(age))

# strings are always true, no characters = false
# this is useful for userinput like if someone skipped putting their name in a sign up page
name = bool(name)
#prints True
print(name)