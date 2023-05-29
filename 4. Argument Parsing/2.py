import sys
import getopt

filename = "test.txt"
message = "This is a test"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

print(opts)
print(args)

for opt, arg in opts:
    if opt in ('-f', '--filename'):
        filename = arg
    elif opt in ('-m', '--message'):
        message = arg

with open(filename, 'w+') as f:
    f.write(message)

# py .\2.py -f test2.txt -m "Hello There!"