#          PASSGEN.PY
#          ----------
# Generates a random password
# string. Can specify a length
# and character type options.
#

import sys, string, random

MINLEN = 4
MAXLEN = 50

# DEF
optList = ['c', 'n', 's']
length = int(random.random() * (MAXLEN - MINLEN + 1) + MINLEN)
password = ''

def usage():
	print("Usage: " + sys.argv[0] + " [password length] [options -> (c)hars, (n)umbers, (s)ymbols]")
	print("E.x: " + sys.argv[0] + " 32 c s")

def fatal(err):
	print("Fatal Error: " + err)
	usage()
	sys.exit(2)

# MAIN
# Parse user args
if len(sys.argv) > 5:
	usage()
	sys.exit(1)

# Parse options
if len(sys.argv) > 2:
	optList = []
	for opt in sys.argv[2:]:
		if len(opt) > 1 or opt not in 'cns':
			fatal("Invalid option specifier")
		optList += opt

# Parse password length
if len(sys.argv) > 1:
	if not sys.argv[1].isdecimal():
		usage()
		sys.exit(1)
	if int(sys.argv[1]) < MINLEN or int(sys.argv[1]) > MAXLEN:
		fatal("Invalid password length (must be 4 to 50)")
	length = int(sys.argv[1])

# Randomly fill password string
for char in range(0, length):
	charType = random.choice(optList)
	if charType is 'c':
		password += random.choice(string.ascii_letters)
	elif charType is 'n':
		password += random.choice(string.digits)
	else:
		password += random.choice(string.punctuation)

print(password)
