# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []
total = 0

print("------------ MENU -----------")
for key, value in menu.items():
    print(f"{key.capitalize():10}: ${value:.2f}")
print("-----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None: # if the food the user selects isn't in the menu, it won't show up in the cart
        cart.append(food)

print("--------- YOUR ORDER --------")

for food in cart:
    total += menu.get(food) # get's the value (price) of the food item
    print(food, end = " ")

print()
print(f"Total is: ${total:.2f}")