# Iterables = an object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers1 = [1, 2, 3, 4 ,5] # lists are iterables

# each element of the iterable should be related to the iterable
# for number in reversed(numbers1):
    # print(number)

numbers2 = (1, 2, 3, 4, 5) # tuples are iterables

# for number in numbers2:
    # print(number)

fruits = {"apple", "orange", "banana", "coconut"} # sets are iterables

# for fruit in fruits: # sets cannot be reversed
    # print(fruit)

name = "John Smith" # strings are iterables

# for character in name:
    # print(character, end = " ")

my_dictionary = {"A": 1, "B": 2, "C": 3}

# for key,values in my_dictionary.items():
    # print(f"{key} = {values}")
