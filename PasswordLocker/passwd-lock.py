import os, string, random, json
from crypt import crypt

LOCKOUT = 5

# DEF
userList = json.load(open("users.json", "r"))

def newUser(user):
    # Set new password
    while True:
        password = input("Enter a new password: ")
        if password != input("Confirm your password: "):
            print("Passwords do not match")
        else:
            break

    # Generate hash
    chars = string.ascii_letters + string.digits
    salt = random.choice(chars) + random.choice(chars)
    userList[user] = crypt(password, salt)

    # Update users.json and create a new user vault file
    json.dump(userList, open("users.json", "w+"))
    json.dump({}, open("vaults/" + user + ".json", "w+"))
    print("Created new user " + user)

def login(user):
    salt = userList[user][:2]
    count = 0
    while True:
        password = input("Enter your master password: ")
        if (crypt(password, salt) == userList[user]):
            return True
        else:
            print("Invalid password")
            count += 1
        if count == LOCKOUT:
            print("Maximum number of tries reached")
            return False

def browse(user):
    return

# MAIN
user = str(os.getuid())

if user not in userList.keys():
    newUser(user)

if login(user):
    browse(user)
