#!/usr/bin/python3

# Made by: ch4tic.
# Github repository: https://github.com/ch4tic/Python-Login-System.git

# Importing libraries.
import time
import os
import sys
import random

# Function for clearing the screen.
def clear():
    os.system('cls')
# Function for a new line.
def new():
    print('\n')
# Function that welcomes the user to the program.
def intro():
    welcomeString = 'Login System'
    print('-' * len(welcomeString))
    print(welcomeString)
    print('-' * len(welcomeString))

def folderMake():
    os.system('d:')
    os.system('mkdir credentials2')
# Sign up function.
def signUp():
    clear()
    intro()
    time.sleep(2)
    # Declares global variables.
    global username
    global password
    username = input('Username: ') # Username input.
    # If user is not entering anything it prompts for input.
    while username == '':
        username = input('Username: ')
    clear()
    intro()
    password = input('Password: ') # Password input.
    # If user is not entering anything it prompts for input.
    while password == '':
        password = input('Password: ')
    # User is prompted for input while the length is less than 8 characters.
    while len(password) < 8:
        new()
        print('Password is too short! (min. 8 characters)')
        time.sleep(1)
        password = input('Password: ')

    # Unlocking the credentials folder.
    os.system('cacls credentials2 /P everyone:f')
    clear()
    intro()
    # Opening the folder.
    file = open(r'D:/ch4tic/Programiranje/Python Programs/Login System/credentials2/' + username + ".txt", "w")
    file.write(username + ":" + password)
    file.close()
    # Locking the folder so no one can access it.
    os.system('cacls credentials2 /P everyone:n')
    clear()
    intro()
    signIn()

# Sign in function.
def signIn():
    clear()
    intro()
    time.sleep(2)
    new()
    while True:
        usrLogin = input("Username: ") # User enters his account username.
        # Program tries to unlock the folder with credentials and open it.
        try:
            os.system('cacls credentials2 /P everyone:f')
            clear()
            intro()
            # Opening the folder with the correct path.
            file = open(r'D:/ch4tic/Programiranje/Python Programs/Login System/credentials2/' + usrLogin + ".txt", "r")
        # If it is not possible, program prints out that it is incorrect.
        except:
            print('Incorrect username!')

        data = file.readline() # Program reads the file.
        pwdLogin = input('Password: ') # User enters his account password
        file.close() # Program exits the file after reading it.
        os.system('cacls credentials2 /P everyone:n') # Program locks the folder and no user can access it.
        clear()
        intro()
        # If credentials are correct, user logs in!
        if data == usrLogin + ':' + pwdLogin:
            print('Welcome!')
            time.sleep(1)
            sys.exit()
        else:
            print("Incorrect username or password.")

# Function for a user to decide whether he wants to sign up or sign in.
def choices():
    time.sleep(2) # Time delay.
    choice = input('Sign up or Sign in?')
    while choice == '':
        choice = input('Sign up or Sign in?')
    if choice == 'Sign up':
        signUp() # Calls a function for sign up.
    elif choice == 'Sign in':
        signIn() # Calls a function for sign in.
    else:
        print('No choice specified!')
        time.sleep(1)
        sys.quit()

# Main function calls all the needed functions.
def main():
    intro() # Welcomes the user to the program.
    folderMake() # Function that makes the credentials folder.
    protect() # Function that protects the folder so no one can access it.
    choices() # User has an option to either sign up or sign in.

main() # Calling the main function.


# Project done: False.
# Deadline: 06.20.2020.
