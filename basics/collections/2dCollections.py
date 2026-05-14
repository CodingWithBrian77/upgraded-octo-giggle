fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
# you can also just use each list rther than giving them a name
# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"] ,
#              ["chicken", "fish", "turkey"]]

# print(groceries[0]) # outputs essentially the fruits list
# print(groceries[0][0]) # outputs apple, if you try to access an index outside of each row/col, IndexError occurs

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print() #outputs similar 2D structure as groceries syntax above