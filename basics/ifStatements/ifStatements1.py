# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 18: # any code under if must be indented
    print("You are now signed up!")
elif age < 0: # can add as many elif statements as you want
    print("You haven't been born yet!")
elif age >= 100: #make sure other conditionals above aren't true before reaching here in order to prevent logic errors
    print("You are too old to be sign up!")
else: #treated as a last resort
    print("You must be 18+ to sign up!")