#!/usr/bin/python3

# Made by: ch4tic.
# Github repository: https://github.com/ch4tic/Python-Login-System.git

# Importing libraries.
import time
import os
import sys
import random

global commands
global path 
commands = ['Change username', 'Reset password', 'Exit']
path = os.getcwd() + '/credentials2/'

# Function for clearing the screen.
def clear():
    os.system('clear')
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
        print('Password is too short! (min. 8 characters)')
        time.sleep(1)
        password = input('Password: ')

    # Unlocking the credentials folder.

    clear()
    intro()
    # Opening the folder.
    file = open(path + username + ".txt", "w")
    file.write(username + ":" + password)
    file.close()
    clear()
    intro()
    signIn()

def tooManyInvalid():
    clear()
    intro()
    print('Commands: ')
    for command in commands:
        print('-' * len(command))
        print(command, sep='\n')
        print('-' * len(command))
        time.sleep(1)
    commandInput = input('Enter a command: ')
    while commandInput == '':
        commandInput = input('Enter a command: ')
    while commandInput not in commands:
        print('Command not available!')
        commandInput = input('Enter a command: ')
    if commandInput == commands[0]:
        usernameChange()
    elif commandInput == commands[1]:
        passwordReset()




# Sign in function.
def signIn():
    clear()
    intro()
    global usrLogin
    global pwdLogin
    global data
    global file
    time.sleep(2)
    usrLogin = input("Username: ") # User enters his account username.
    # Program tries to unlock the folder with credentials and open it.
    try:
        clear()
        intro()
        # Opening the folder with the correct path.
        file = open(path + usrLogin + ".txt", "r")
    # If it is not possible, program prints out that it is incorrect.
    except:
        print('Incorrect username!')
    data = file.readline() # Program reads the file.
    pwdLogin = input('Password: ') # User enters his account password
    file.close() # Program exits the file after reading it.
    clear()
    intro()
    # If credentials are correct, user logs in!
    if data == usrLogin + ':' + pwdLogin:
        print('Welcome ' + str(usrLogin) + '!')
        time.sleep(1)
        print('Commands: ')
        for command in commands:
            print('-' * len(command))
            print(command, sep='\n')
            print('-' * len(command))
            time.sleep(1)
        commandInput = input('Enter a command: ')
        while commandInput == '':
            commandInput = input('Enter a command: ')
        while commandInput not in commands:
            print('Command not available!')
            commandInput = input('Enter a command: ')
        if commandInput == commands[0]:
            usernameChange()
        elif commandInput == commands[1]:
            passwordReset()
        elif commandInput == commands[2]: 
            clear() 
            intro()
            print('Goodbye my friend!')
            time.sleep(1)
            sys.exit()
    else:
        print("Incorrect username or password.")

def usernameChange():
    clear()
    intro()
    currentUsername = input('Enter current username: ')
    while currentUsername == '' or currentUsername != usrLogin:
        currentUsername = input('Enter current username: ')
    if currentUsername == usrLogin:
        print('Username is valid.')
        newUsername = input('New username: ')
        while newUsername == '':
            newUsername = input('New username: ')
        clear()
        intro()
        file = open(path + newUsername + ".txt", "w")
        file.write(newUsername + ":" + pwdLogin)
        file.close()
        os.chdir('credentials2')
        os.system('rm ' + usrLogin + '.txt')
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
        sys.exit()

# Main function calls all the needed functions.
def main():
    intro() # Welcomes the user to the program.
    folderMake() # Function that makes the credentials folder.
    choices() # User has an option to either sign up or sign in.

main() # Calling the main function.

# Project done: Done.
# Deadline: 06.20.2020.
