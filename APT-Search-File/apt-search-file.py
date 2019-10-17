#     APT-SEARCH-FILE.PY
#     ------------------
# Performs an 'apt search' on
# each entry within a newline
# separated list.
#

# TODO: Prevent the user from being able to modify apt search option arguments

import sys
import os

# DEF
def usage():
    print("Usage: {:s} [package list]".format(sys.argv[0]))
    sys.exit(1)

def fileSize(fd):
    fd.seek(0, 2)
    size = fd.tell()
    fd.seek(0, 0)
    return size

# MAIN
if len(sys.argv) != 2:
    usage()
try:
    fd = open(sys.argv[1])
except FileNotFoundError:
    print("Fatal Error: Failed to open file '{:s}'".format(sys.argv[1]))
    sys.exit(2)

print('')

fSize = fileSize(fd)
fString = fd.read(fSize)
package = ''
for char in fString:
    if char is '\n':
        os.system("echo '{0:s}'; echo {2:s}; apt show '{1:s}'; echo".format(package.upper(), package, len(package) * '-'))
        package = ''
    else:
        package += char

fd.close()
