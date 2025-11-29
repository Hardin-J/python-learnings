# Exercise 3.2 – Login System
# Ask username & password. If match → Access Granted else Access Denied.



def createCred():
    print("----- Create Credential System -----")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    return username, password

def login(username, password):
    print("----- Login System -----")
    name = input("Enter username: ")
    _word = input("Enter password: ")
    
    if name == username and _word == password:
        print("Access Granted.")
    else:
        print("Access Denied.")

username, password = createCred()
login(username, password)