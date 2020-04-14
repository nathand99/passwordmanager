#!/bin/python3
import getpass
from pathlib import Path
import os
import cryptography
from cryptography.fernet import Fernet
import random
import string


# Something Awesome project for COMP6841. Written by Nathan Driscoll (z5204935)

# A program to store passwords securely

# global list of dictionaries containing records
records = []
# path for file used to store data
path = Path("psdata.txt")
# path for file used to store key (encrypted)
secret_key = Path("secret_key.txt")

# key used to encrypt key (hardcoded)
my_key = b'oxAH5eINZEzXSNsfP3PpPyi3Jt92-gwVrVfQHaVlvpA='
#my_key = str.encode(my_key_str)

# functions

# signup - create username and password
# also create file and store login details in it as well as store key in key file
def signup():
    while True:
        username = input("Please enter a username: ")
        print("Please create a master password. Ensure it is secure and memorable")
        master = getpass.getpass("Create master password: ")
        check = getpass.getpass("Retype master password: ")   
        if master != check:
            print("\n")
            print("Passwords do not match! Please try again\n")
            continue
        else:
            print("Password successfully created!")
            print("Please remember this password as there is NO WAY to access this account without the master password\n")
            break
    print("Welcome {}!\n".format(username))
    # generate, encrypt and write key to file
    key = Fernet.generate_key()
    encrypted_key = encrypt_key(key)
    with open(secret_key, "wb") as f:        
        f.write(encrypted_key)
    with open(path, "wb") as f:  
        # write username and password to first line
        record = "thisapplication" + "," + username + "," + master + "||"
        encrypted = encrypt_text(record, key)
        f.write(encrypted)      
    # add record of this account to records
    entry = {"account": "thisapplication" , "username": username, "password": master}
    records.append(entry) 


# login - if master password is correct, user is let in
def login():
    print("Hi {}!".format(records[0].get("username")))
    while True:
        passwo = input("Please enter master password: ")
        if passwo == records[0].get("password"):
            break
        else:
            print("Incorrect password entered. Please try again")

# read encrypted key from file
def read_key():
    with open(secret_key, "rb") as f:
        encrypted_key = f.read()
        key = decrypt_key(encrypted_key)
        return key

# read data out of file into list of dictionaries. Also read in key
def read_data():
    key = read_key()
    with open(path, "rb") as f:
        data = f.read()
        string = decrypt_text(data, key)
        entries = string.split("||")
        for entry in entries:
            if entry == "":
                break
            # split line from file by separater
            new_line = entry.split(",")
            # remove newline from end of line (in password)
            #new_password = new_line[2][:-1]
            entry = {"account": new_line[0] , "username": new_line[1], "password": new_line[2]}
            records.append(entry)    

# print all entries in records list
def print_data():
    '''
    print("\t" + "Account" + "\t|\t" + "Username" + "\t|\t" + "Password")
    print("-----------------------------------------------------------------------")
    for entry in records:
        print(entry.get("account") + "\t|\t" + entry.get("username") + "\t|\t" + entry.get("password"))
    '''
    dash = '-' * 79
    print(dash)
    print("|{:^25s}|{:^25s}|{:^25s}|".format("Account", "Username", "Password"))
    print(dash)
    for entry in records:
        print("|{:^25s}|{:^25s}|{:^25s}|".format(entry["account"], entry["username"], entry["password"]))
    print(dash)

# print details for a specific account given a record in records
def print_row(record):
    dash = '-' * 79
    print(dash)
    print("|{:^25s}|{:^25s}|{:^25s}|".format("Account", "Username", "Password"))
    print(dash)
    print("|{:^25s}|{:^25s}|{:^25s}|".format(record["account"], record["username"], record["password"]))
    print(dash)

# add a record
def add_record():
    acc = input("Enter account: ")
    user = input("Enter username: ")
    passw = input("Enter password (to generate a password, press the letter g then enter): ")
    # generate a random password length 15 for user
    if passw == "g":
        randomtext = string.ascii_letters + string.digits
        passw = ''.join(random.choice(randomtext) for i in range(15))
    new_entry = {"account": acc, "username": user, "password": passw}
    records.append(new_entry)
    print("New record created successfully!")
    print_row(new_entry)

#edit a record
def edit_record(record):
    print("Current status: ")
    print_row(record)
    print("Modifying record: ")
    acc = input("Enter account: ")
    user = input("Enter username: ")
    passw = input("Enter password (to generate a password, press the letter g then enter): ")
    # generate a random password length 10 for user
    if passw == "g":
        randomtext = string.ascii_letters + string.digits
        passw = ''.join(random.choice(randomtext) for i in range(15))
    record["account"] = acc
    record["username"] = user
    record["password"] = passw
    print("Edit successful!, updated record: ")
    print_row(record)
# write records list to file (overwritting contents of file)
def save():   
    key = read_key()
    wr = open(path, 'wb')
    # compile all records into a single string
    string = ""
    for record in records:   
        string = string + record.get("account") + "," + record.get("username") + "," + record.get("password") + "||"
    # encrypt and write string to file
    encrypted = encrypt_text(string, key)
    wr.write(encrypted)  

# encrypt file - takes in plaintext and returns excrypted bytes
def encrypt_text(text, key):
    f = Fernet(key)
    # str -> bytes
    b_text = text.encode()
    encrypted = f.encrypt(b_text)
    return encrypted
# decrypt file - takes in encrypted bytes and returns plaintext
def decrypt_text(encrypted, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    s_decrypted = decrypted.decode("utf-8")
    return s_decrypted
# encrypt key
def encrypt_key(text):
    f = Fernet(my_key)
    encrypted = f.encrypt(text)
    return encrypted
# decrypt key
def decrypt_key(encrypted):
    f = Fernet(my_key)
    decrypted = f.decrypt(encrypted)
    return decrypted

##################################################################################

# first time running the program? If yes, then "psdata.txt" exists
first_time = True
if path.is_file():
    first_time = False

print("Welcome to Password Storer!\n")

if first_time:
    # signup - get username and password from user and store in records 
    signup()
    print("Now let's enter the first account, username and password")
    add_record()
else:
    # returning user
    # read data in from from file into records
    read_data()      
    # login user
    login()

# inside program now

print("Login Successful. Welcome back {}!\n".format(records[0].get("username")))
# print account | username | password for all records
print("Your records: ")
print_data()
# loop to enter commands
print("Type 'help' to view commands")
while True:
    user_input = input("Enter a command: ")
    command = user_input.split()
    if command[0] == "records":
        print_data()
    elif command[0] == "add":
        add_record()
    # view account - print record with corresponding account name
    elif command[0] == "view":
        if len(command) == 1:
            print_data()
            continue
        found = False
        for record in records:
            if record.get("account") == command[1]:
                print_row(record)
                found = True
                break
        # no records with that account name
        if found == False:
            print("No record for an account with account name: '{}'".format(command[1]))
    elif command[0] == "edit":
        for record in records:
            if record.get("account") == command[1]:
                edit_record(record)
    elif command[0] == "delete":
        if command[1] == "thisapplication":
            print("Cannot delete this account!")
            continue
        check = input("Are you sure you want to delete the record for '{}'? (y|n): ".format(command[1]))
        if (check != "y"):
            print("Deletion ABORTED")
            continue
        for record in records:
            if record.get("account") == command[1]:
                records.remove(record)
                print("Record for '{}' deleted successfully".format(command[1]))
                break               
    elif command[0] == "deleteaccount":
        yesorno = input("Are you sure you want to delete your account? All data will be lost (y/n): ")
        if yesorno == "y":
            os.remove(path)
            os.remove(secret_key)
            print("Account deletion SUCCESSFUL. Program will now terminate")
            exit()
        else:
            print("Account deletion ABORTED")
            continue
    elif command[0] == "help":
        print("'records': display all records")
        print("'add': add a new record")
        print("'view [ACCOUNT NAME]': view the record for ACCOUNT NAME")
        print("'edit [ACCOUNT NAME]': edit the record for ACCOUNT NAME")
        print("'delete [ACCOUNT NAME]': delete the record for ACCOUNT NAME")
        print("'deleteaccount': delete your password storer account")
        print("'help': display this block of text")
        print("'save': save additions and changes you have made to records to file")
        print("'quit': save and exit program")    
    elif command[0] == "save":
        save()
    elif command[0] == "quit":
        #save then quit
        save()
        exit()
    elif command[0] == "fox1":
        print("FOX 1!")
    elif command[0] == "fox2":
        print("FOX 2!")
    elif command[0] == "fox3":
        print("FOX 3!")
    else:
        print("Unknown command. Type 'help' for list of commands")
exit()