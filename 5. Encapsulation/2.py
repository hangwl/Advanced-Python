
# basic idea is that we don't we want users to have direct writing access to the variables
# however real encapsulation is not a real thing in Python since we can always have accces to _private variables through object's __dict__ method

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def Name(self):
        return self._name
    
    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self._name = "Not Bob"
        else:
            self._name = value

p1 = Person("Hang", 25)
print(p1.Name)

p1.Name = "Bob"
print(p1.Name)
