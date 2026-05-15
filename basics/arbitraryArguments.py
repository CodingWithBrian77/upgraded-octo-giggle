# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY


def add(*args): # *args packs arguments into a tuple, name doesn't matter just * matters
    total = 0
    for arg in args:
        total += arg
    return total

# print(add(1, 2, 3, 4, 5))

def print_address(**kwargs): # **kwargs packs arguments into a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_address(street="123 Fake St.",
#             apt="100",
#             city="Detroit",
#             state="MI",
#             zip="54321")

def shipping_label(*args, **kwargs): # **kwargs must follow *args
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               pobox = "PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")