# default arguments = a default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount=0, tax=0.05): # sets discount and tax with a default value, but in the invoking call, the arguments from there will change the discount or tax if given
    return list_price * (1-discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1))

import time

def count(end, start=0): # default needs to follow a non-default argument
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(30, 15)

