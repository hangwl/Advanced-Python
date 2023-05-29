# Encapsulation in Python describes the concept of bundling data and methods within a single unit
# it offers 1. Data Protection, 2. Modularity and 3. Abstraction

# when you are implementing a class, you are implementing encapsulation, and
# this puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data
# to prevent accidental change, an object's variable can only be changed by an object's method call

# consider a real-life example of encapsulation
# in a company, there are different sections like the accounts section, finance section, sales section, etc.
# the finance section handles all the sales-related activities and keeps records of all the sales
# if for some reason an officer from the finance section needs the data of the sales section,
# he will have to contact some other officer in the sales section and then request for the sales data
# this is what encapsulation is, and it hides diffent sections of data from any other section

# 1. Protected Members
# protected members of the class cannot be accessed outside the class but can be accessed from within the class and its subclasses
# in Python, we set the prefix of a single underscore "_" to the member

# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of Base class
		Base.__init__(self)
		print("Calling protected member of base class: ", self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ", self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)


# 2. Private Members
# class members declared private should neither be accessed outside the class nor by any base class
# In Python, there is no existence of Private instance variables
# to define a private member, we set prefix of a double underscore "__" to the member


# Creating a Base class
class Base2:
	def __init__(self):
		self.a = "Monka"
		self.__c = "Giga"

# Creating a derived class
class Derived2(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj3 = Base2()
print(obj3.a)

# print(obj3.__c)
# obj4 = Derived2()

# Uncommenting print(obj3.c) will raise an AttributeError
# Uncommenting obj4 = Derived2() will also raise an AttributeError as private member of base class is called inside derived class
