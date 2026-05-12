# Python calculator

operator = input("Enter an operator (+ - * /)")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

# Without typecasting them as float/int, this creates string concatenation, not needed for this program
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)

