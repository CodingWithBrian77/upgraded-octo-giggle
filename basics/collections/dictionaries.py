# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("USA")) # returns None if key doesn't exist

# Basic key check if-else block
# if capitals.get("Russia"):
    # print("That capital exists")
# else:
    # print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"}) # inserts key:value pair at the end of dictionary
# capitals.update({"USA": "Detroit"}) # updates existing key with a new value
# capitals.pop("China") # removes a key:value pair
# capitals.popitem() # removes most recently added key:value pair
# capitals.clear() # removes all key:value pairs
# keys = capitals.keys() # displays only keys

# for key in capitals.keys(): # can iterate over keys and print individually
    # print(key)

# values = capitals.values() #displays only values
# print(values)

# items = capitals.items() #displays a 2D list of tuples
# for key,value in capitals.items(): #iterates using 2 counters (key, value)
    # print(f"{key}: {value}") #displays key: value pair without [{, etc.