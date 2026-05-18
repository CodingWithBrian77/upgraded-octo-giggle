# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attrbiutes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car: #car meets animal class requirements to be considered an animal

    alive = False

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)