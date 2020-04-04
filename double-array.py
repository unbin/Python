import sys
from sys import argv

# DEF
def usage():
    print("Usage: {} [TOP ARRAY NUM] [INNER ARRAY NUM]".format(argv[0]))

def fatal(err):
    print("Fatal: " + err);
    usage()
    sys.exit(1)

# MAIN
# User input
if len(argv) != 3:
    fatal("Invalid number of arguments.")
if not argv[1].isdecimal() or not argv[2].isdecimal():
    fatal("Invalid argument type (must be a positive whole number).")

topArrNum = int(argv[1])
innerArrNum = int(argv[2])

# Init
arr = []
for i in range(0, topArrNum):
    arr.append([0] * innerArrNum)

# Fill Array
print("Arr before loop:\n", arr)

count = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        count += 1
        arr[x][y] = count

print("Arr after loop:\n", arr)
