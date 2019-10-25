#          WEB-DOWNLOADER.PY
#          =================
# Downloads a website from the specified
# URL and stores it in a file.
#

from sys import argv
import requests
from bs4 import BeautifulSoup

# DEF
def usage():
	print("Usage: {} [URL] [output filename]".format(argv[0]))

# MAIN
if len(argv) != 3:
	usage()
	exit(1)

# Get website
res = requests.get(argv[1])
res.raise_for_status()

# Write to file
fd = open(argv[2], 'wb')
soup = BeautifulSoup(res.text, "html.parser")
fd.write(soup.prettify().encode())
fd.close()
