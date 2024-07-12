import random
import time
import os

# inputs
username = ["Kimmy", "Kim", "Kimberly"]
passcode = ["Kimmy123","Kim123", "Kimberly123"]
bank_options = ["Check Balance", "Withdraw", "Deposit", "Log to another Account", "Quit"]
Balance = [1000, 7000, 15000]  # Initial balance, adjust as needed

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcomemessage():
    print(f'\n-----------------------------------\nWelcome to BEL Banking!\n-----------------------------------')

def login():
    user_input = input("Enter your username: ")
    pass_input = input("Enter your password: ")
    access_check(user_input, pass_input)

def access_check(user_input, pass_input):
    if user_input in username and pass_input == passcode[username.index(user_input)]:
        print(f'Access Granted for {user_input}!')
        print('Entering account', end="")
        for dot in range(3):
            time.sleep(1)
            print(".", end="", flush = True)
        presentchoices(user_input)
    else:
        print(f'Access Denied!')
        login()

def presentchoices(user_input):
    i = 1
    print(f'\nChoose only one from the following options:')
    for option in bank_options:
        print(f'[{i}]  {option}')
        i+= 1
    print(f'-----------------------------------')
    get_userchoice(user_input)

def get_userchoice(user_input):
    try:
        user_action = int(input("Choose an action: ").strip().title())
        if user_action == 1:
            checkbalance(user_input)
        elif user_action == 2:
            withdraw(user_input)
        elif user_action == 3:
            deposit(user_input)
        elif user_action == 4:
            login()
        elif user_action == 5:
            quit()
        else:
            print("Invalid choice.")
            get_userchoice(user_input)

    except ValueError:
        print("Please enter a number.")
        get_userchoice(user_input)

def checkbalance(user_input):
    user_index = username.index(user_input)
    print(f"Your current balance is: ${Balance[user_index]}.")
    presentchoices(user_input)

def withdraw(user_input):
    user_index = username.index(user_input)
    withdraw_amt = int(input("Enter amount to be withdrawn: "))
    if Balance[user_index] >= withdraw_amt:
        Balance[user_index] -= withdraw_amt
        print(f'Withdrawing {withdraw_amt}', end="")
        for dot in range(3):
            time.sleep(1)
            print(".", end="", flush = True)
        print(f"${withdraw_amt} has been successfully withdrawn from your account!")
    else:
        print(f"Insufficient balance. You cannot withdraw {withdraw_amt}.")
    presentchoices(user_input)

def deposit(user_input):
    user_index = username.index(user_input)
    deposit_amt = int(input("Enter amount to be deposited: "))
    Balance[user_index] += deposit_amt
    print(f'Depositing {deposit_amt}', end="")
    for dot in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print(f"${deposit_amt} has been successfully deposited to your account!")
    presentchoices(user_input)

def quit():
    print(f"Thank you for banking with us!")
    exit()

welcomemessage()
login()