import sys, os, json
from crypt import crypt

def newUser(user, userList):
    # New Password
    while True:
        password = input("Enter a new password: ")
        confirm = input("Confirm your password: ")
        if password != confirm:
            print("Passwords do not match")
        else:
            break
    # Add to list and update users file
    userList[user] = crypt(password, "AA")
    json.dump(userList, open("users.json", "w"))
    print("Password registered")

def login(password):
    return

# MAIN
userList = json.load(open("users.json", "r"))
user = str(os.getuid())

if user not in userList.keys():
    newUser(user, userList)

login(input("Enter your master password: "))
