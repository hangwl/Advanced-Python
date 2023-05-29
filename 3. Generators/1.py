import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(10000) # size of generator will not change!
print(sys.getsizeof(values)) 

for x in values:
    print(x)
