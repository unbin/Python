#       File Encrypt.py
#       ===============
#   XOR Encrypts a file with
#   the supplied key.
#

from sys import argv, exit
import sys
import os

DEBUG = True

# DEF

def usage():
    print("Usage: " + argv[0] + " <File Path> <Key>")
    exit(1)

# Read blocks from file_in, xor encrypt, and write to file_out
def encrypt(file_in, file_out):
    file_out.write("Encryption Not Implemented Yet!\n".encode("utf-8"))

# END DEF

# MAIN

# Check arguments
if (len(argv) != 3):
     usage()

# Check if file exists
if not os.path.exists(argv[1]):
    print("Error: Path file name not found!", file=sys.stderr)
    exit(1)

if not os.path.isfile(argv[1]):
    print("Error: File must be a normal file.", file=sys.stderr)
    exit(1)

file_size = os.path.getsize(argv[1])
if DEBUG:
    print("[DEBUG] File Size: {} Bytes".format(file_size))

with open (argv[1], "rb") as file_in:
    if DEBUG:
            print("[DEBUG] File " + file_in.name + " Opened.")

    with open(argv[1] + ".encrypted", 'wb') as file_out:
        if DEBUG:
            print("[DEBUG] File " + file_out.name + " Opened.")

        encrypt(file_in, file_out)

        file_out.close()
    file_in.close()

# END MAIN
