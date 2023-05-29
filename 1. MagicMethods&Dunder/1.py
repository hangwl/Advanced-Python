class Person:

    def __init__(self, name, age): # init is the constructor
        self.name = name
        self.age = age

    def __del__(self): # del is the deconstructor
        print("Object is being deconstructed!")

p = Person("Mike", 25)