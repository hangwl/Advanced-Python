# rather than storing a collection of previous values, the function simply yields the next value, thus saving memory

def infinite_seq():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_seq()

for x in range(500):
    print(next(values))
 