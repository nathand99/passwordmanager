#!/bin/python3
import getpass
from pathlib import Path
import os

# A program to store passwords securely

# list of dictionaries containing data
records = []
# path for file used to store data
path = Path("psdata.txt")

# functions

# signup - create username and password. ALso create file and store login details in it
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
    # create file 
    f = open(path,"w")
    # write username and password to first line
    f.write("thisapplication" + "," + username + "," + master + "\n")
    # add record of this account to records
    # the login details for this program will always be on line 1
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

# read data out of file into list of dictionaries
def read_data():
    with open(path) as f:
        for line in f:
            # split line from file by separater
            new_line = line.split(",")
            # remove newline from end of line (in password)
            new_password = new_line[2][:-1]
            entry = {"account": new_line[0] , "username": new_line[1], "password": new_password}
            records.append(entry)  
            #print(records)

# print entries in data
def print_data():
    print("\t" + "Account" + "\t|\t" + "Username" + "\t|\t" + "Password")
    print("-----------------------------------------------------------------------")
    for entry in records:
        print(entry.get("account") + "\t|\t" + entry.get("username") + "\t|\t" + entry.get("password"))

# print details for a specific account given a record in records
def print_row(record):
    print(record.get("account") + "\t|\t" + record.get("username") + "\t|\t" + record.get("password"))

# add a record
def add_record():
    acc = input("Enter account: ")
    user = input("Enter username: ")
    passw = input("Enter password: ")
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
    passw = input("Enter password: ")
    record["account"] = acc
    record["username"] = user
    record["password"] = passw
    print("Edit successful!, updated record: ")
    print_row(record)
# write records list to file (overwritting contents of file)
def save():   
    wr = open(path, 'w')
    for record in records:
        wr.write(record.get("account") + "," + record.get("username") + "," + record.get("password") + "\n")  

''' 
# encrypt file
def encrypt_file():

# decrypt file
def decrypt_file():
'''
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
    # login
    login()

# inside program now


print("Login Successful. Welcome back {}!\n".format(records[0].get("username")))
# print account | username | password for all records
print("Your records: ")
print_data()
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
        yesorno = input("Are you sure you want to delelte your account? All data will be lost (y/n): ")
        if yesorno == "y":
            os.remove(path)
            print("Account deletion SUCCESSFUL. Program will now terminate")
            exit()
        else:
            print("Account deletion ABORTED")
            continue
    elif command[0] == "help":
        print("'records': display all records")
        print("'add': allows user to add a new record")
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