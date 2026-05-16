# variable scope = where a variable is visisble and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()

from math import e

def func1():
    print(e)

e = 3 # this creates 2 different versions of e (global and built-in versions)

func1()