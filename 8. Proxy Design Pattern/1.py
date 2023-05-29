# proxy basically wraps functionality around the object creation, introducing another layer of abstraction over instances of classes

from abc import ABCMeta, abstractmethod # used for defining abstract base classes and abstract methods

class IPerson(metaclass=ABCMeta): # metaclass=ABCMeta argument indicates that IPerson is an abstract class
    @abstractmethod
    def person_method(self): # the person_method is an abstract method that any subclass of IPerson must implement, and serves as the interface method that represents the behavior of a person
        """Interface Method"""

# define Person class that inherits from IPerson, and implements the person_method, which prints "I am a person"
# the Person class represents the actual implementation of a person
class Person(IPerson):
    def person_method(self):
        print("I am a person")

# the following code defines a proxy class that also inherits from IPerson, and acts as a proxy for the Person class
# in the __init__ method, it initializes an instance attribute 'self.person' as an instance of the Person class
# in the person_method method, it adds additional functionality by printing "I am the proxy functionality" before delegating the person_method call to the self.person.person method()
class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality")
        self.person.person_method()

p1 = Person()
p1.person_method()  # Output: I am a person

p2 = ProxyPerson()
p2.person_method()  # Output: I am the proxy functionality
                    #         I am a person


