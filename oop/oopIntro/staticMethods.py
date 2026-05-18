# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to clas data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self): # instance method
        return f"{self.name} = {self.position}"
    
    @staticmethod # static methods belong only to the class and not the objects
    def is_valid_position(position): # static methods
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Euguene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Manager")) # must call the class and then the static method

print(employee1.get_info()) # instance method calls
print(employee2.get_info())
print(employee3.get_info())