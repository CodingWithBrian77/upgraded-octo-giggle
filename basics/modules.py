# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

import math
# can give modules aliases
# import math as m #imports math module (variables and functions)
# from math import e #can import specific parts of the module

a, b, c, d, e = 1, 2, 3, 4, 5

# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

import exampleModule

result1 = exampleModule.pi
result2 = exampleModule.square(3)
result3 = exampleModule.cube(3)
result4 = exampleModule.circumference(3)
result5 = exampleModule.area(3)
print(result5)
