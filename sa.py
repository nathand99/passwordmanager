#!/bin/python3
from getpass import getpass
from pathlib import Path

# A program to store passwords securely

# first time running the program? 
# If yes, then "psdata.txt" exists
first_time = True
path = Path("psdata.txt")
if path.is_file():
    False

print("Welcome to Password Storer!\n")

if first_time:
    # signup
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
    # when out of this loop, create file and place username and password inside
    # create file 
    #f = open("psdata.txt","w+")
else:
    # login
    print("login")

# inside program now
print("Welcome {}!\n".format(username))

# with open(psdata.txt) as file:

if first_time:
    print("Now let's enter the first account, username and password")
    add_record()

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
elif: input[0:3] == "edit":
    fdf
    
# encrypt file
def encrypt_file():

# decrypt file
def decrypt_file():

# read data out of file
def read_data():
    #for each line after the first
    #read
    #separate line by ","
    #print out record | separated

# add a record
def add_record():
    acc = input("Enter account: ")
    user = input("Enter username: ")
    passw = input("Enter password: ")
    with open(path) as file:
        file.write(acc + "," + user + "," + passw + "\n")
