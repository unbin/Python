#          RANDLOOP.PY
#          -----------
# Infinitely prints psudo-random
# numbers between the [Min] and 
# [Max] arguments (inclusive).
#

import sys
import random

# DEF
def usage():
    print("Usage: " + sys.argv[0] + " [Min] [Max]")

def fatal(err):
    print("Fatal: " + err)
    usage()
    sys.exit(1)

# MAIN

# Check Input
if len(sys.argv) != 3:
    fatal("Invalid number of arguments.")

try:
    min = int(sys.argv[1])
    max = int(sys.argv[2])

except ValueError:
    fatal("Invalid argument type.")

if max < min:
    fatal("Max must be greater than min.")

# Calculate
if min < 0:
    min -= 1

range = max - min + 1

while True:
    print(int(random.random() * range + min))
