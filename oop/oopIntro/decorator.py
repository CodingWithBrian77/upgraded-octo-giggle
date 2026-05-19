# Decorator = A function that extends the behavor of another function
#             w/o modifying the base function
#             Pass the ase function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkes(func):
    def wrapper(*args, **kwargs): # must have this here
        print("*You added sprinkles! 🧁*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You added fudge! 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkes
@add_fudge # you can add multiple decorators to a function
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla")