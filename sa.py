#!/bin/python3
import getpass
from pathlib import Path

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
    # create file 
    f = open("psdata.txt","w+")
    # write username and password to first line
    f.write("thisapplication" + "," + username + "," + master + "\n")

# login - if master password is correct, user is let in
def login():
    print("Welcome back {}!\n".format(records[0].get("username")))
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
            line.split(",")
            entry = {"account": line[0] , "username": line[1], "password": line[2]}
            records.append(entry)  

# print entries in data
def print_data():
    for entry in records:
        print(entry.account + "|" + entry.username + "|" + entry.password)

# add a record
def add_record():
    acc = input("Enter account: ")
    user = input("Enter username: ")
    passw = input("Enter password: ")
    new_entry = {"account": acc, "username": user, "password": passw}
    records.append(new_entry)
    print(records)
    '''
    with open(path) as file:
        file.write(acc + "," + user + "," + passw + "\n")
    '''

##################################################################################

# first time running the program? If yes, then "psdata.txt" exists
first_time = True

if path.is_file():
    first_time = False

print("Welcome to Password Storer!\n")

if first_time:
    # get username and password from user and store in records 
    signup()
    print("Now let's enter the first account, username and password")
    add_record()
else:
    # returning user
    # read data in from from file into records
    file = open(path, "r") 
    temp = file.readline()
    temp.split(",")
    dictionary = {"account": "this application" , "username": temp[1], "password": temp[2]}
    records.append(dictionary)              
    # need to write to file as well
    # login
    login()


# inside program now

print("Welcome {}!\n".format(records[0].get("username")))

# with open(psdata.txt) as file:

    
# print account | username | password for all records
read_data()


'''
print("Press [1] to view passwords")
print("Press [1] to view passwords")
print("Press [1] to view passwords")
'''
input = input()

if input == 1:
    read_data()
elif input[0:3] == "edit":
    print("edit")
''' 
# encrypt file
def encrypt_file():

# decrypt file
def decrypt_file():
'''
