import sys

# Usage: main.py FILENAME "message"
fname = sys.argv[1]
message = sys.argv[2]

with open(fname, 'w+') as f:
    f.write(message)

# py .\1.py test.txt "Hello World!"

# see argparse?