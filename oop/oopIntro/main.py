from car import Car

# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object


car1 = Car("Sentra", 2022, "Grey", False)
car2 = Car("Impala", 2013, "White", True)
car3 = Car("Rogue", 2021, "White", False)

car1.describe()
car2.describe()
car3.describe()