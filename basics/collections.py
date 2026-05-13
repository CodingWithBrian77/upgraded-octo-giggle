# collection = single "variable used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# -- LISTS -- #
fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits)) # displays methods that, that collection type can use
# print(help(fruits))

# print(len(fruits)) # total number of elements in collection
# print("apple" in fruits) # displays boolean value if a string/element is found in collection
# print(fruits[0]) # if you try to access an element that's not in the collection, an IndexError occurs

# fruits[0] = "pinapple" # can change elements by using indexes
# fruits.append("pineapple") # adds an element at the end of the collection
# fruits.remove("apple") # removes the element given
# fruits.insert(0, "pineapple") # adds an element at that specific index
# fruits.sort() # sorts collection in alphabetical order
# fruits.reverse() # reverses order of collection
# fruits.clear() # removes all elements in collection
# print(fruits.index("apple")) # returns index of the given element, ValueError occurs if not found
# print(fruits.count("banana"))

# for fruit in fruits: # for every fruit in fruits
    #print(fruit) # outputs each element on a new line

# -- SETS -- #
cars = {"sedan", "truck", "suv", "hatchback"}
# cars.add("compact sedan") # adds an element 
# cars.remove("compact sedan") # removes the element
# cars.pop() # randomly removes the first element in the collection, although this is random
# cars.clear() # removes all elements in collection

# print(cars[0]) # cannot use index on a set, as it's unordered

# -- TUPLES -- #
foods = ("pizza", "sushi", "ramen", "chicken")
# print(len(foods))
# print("burger" in foods)
# print(foods.index("pizza"))
# print(foods.count("sushi"))

# for food in foods:
    # print(food)



