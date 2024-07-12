import random
import time
import os

# inputs
possible_actions = ["Rock", "Paper", "Scissors"]
Total_Games_Played = 1
Total_Wins = 0
Total_Loss = 0


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def welcomemessage():
    print(f'\nWelcome to Rock-Paper-Scissors Game!')


def presentchoices():
    print(f'             Game No. {Total_Games_Played}')
    print(f'-----------------------------------\nChoose only one from the following options:')
    for choice in possible_actions:
        print(choice)
    print(f'-----------------------------------')


def main():
    global user_action
    global pc_action
    presentchoices()
    get_userchoice()
    pc_action = get_pcchoice()
    print(f'-----------------------------------')
    get_gameresult(user_action, pc_action)


def get_userchoice():
    global user_action
    user_action = input("Your choice is: ").strip().title()


def get_pcchoice():
    print("Waiting for PC", end="")
    for dot in range(9):
        time.sleep(0.21)
        print(".", end="", flush=True)
    pc_action = random.choice(possible_actions)
    print(f'\rPC chose {pc_action}.    ')  # Print PC's choice, overwrite "Waiting for PC..." with spaces



def get_gameresult(user_action, pc_action):
    global Total_Wins
    global Total_Loss
    if user_action == pc_action:
        print(f"You both chose {user_action}. It's a tie!\n***********************************\n")
    elif (user_action == "Rock" and pc_action == "Scissors") or (user_action == "Paper" and pc_action == "Rock") or (
            user_action == "Scissors" and pc_action == "Paper"):
        print(f"You win!\n***********************************\n")
        Total_Wins += 1
    else:
        print(f"You lose!\n***********************************\n")
        Total_Loss += 1


def exitmessage():
    print(f'Thank you for playing! You made a total of')
    get_gamestats()


def get_gamestats():
    print(f'{Total_Games_Played} Game/s,')
    print(f'{Total_Wins} total wins, and')
    print(f'{Total_Loss} total losses')


def PlayAgain():
    global Total_Games_Played
    while True:
        try:
            Continue_Playing = input(f"Would you like to continue playing? (Y/N): ").strip().capitalize()
            if Continue_Playing == "Y":
                clear_screen()
                Total_Games_Played += 1
                main()
            elif Continue_Playing == "N":
                clear_screen()
                exitmessage()
                break
        except ValueError:
            pass


if __name__ == "__main__":
    welcomemessage()
    main()
    PlayAgain()