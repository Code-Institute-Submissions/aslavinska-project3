import random
import gspread
from google.oauth2.service_account import Credentials

# The SCOPE lists the APIs that the program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3')

records = SHEET.worksheet('records')

data = records.get_all_values()
print("Welcome to Rock, Paper, Scissors game. \n")
print("Winnin rules of the game are: \n Paper beats rock \n Rock beats scissors \n Scissors beats paper \n")

def get_user_choice():
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    # Take user input
    user_choice = int(input("Enter a your choice here: "))
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a valid choice please: "))
    if user_choice == 1:
        user_choice_name = 'Rock'
    elif user_choice == 2:
        user_choice_name = 'Paper'
    else: 
        user_choice_name = 'Scissors'
    print("User choice is \n", user_choice_name)
    return user_choice

def get_computer_choice():
    print('Now it is the Computers turn....')
    computer_choice = random.randint(1, 3)
         
    # initialize value of computer_choice_name
    # variable corresponding to the choice value
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissors'

    print("Computer choice is \n", computer_choice_name)
    return computer_choice

def condition_check():
    user_selection = int(get_user_choice())
    print(user_selection)
    computer_selection = int(get_computer_choice())
    print(computer_selection)
    computerscore = 0
    userscore = 0
    # check draw
    if user_selection == computer_selection:
        print("It is a Draw \n", end="")
    # condition for winning
    if (user_selection == 1 and computer_selection == 2):
        print("Player won, paper wins => \n", end="")
        userscore = userscore + 1
    elif (user_selection == 2 and computer_selection == 1):
        print("Computer won, paper wins => \n", end="")
        computerscore = computerscore + 1
    if (user_selection == 1 and computer_selection == 3):
        print("Player won, Rock wins=>\n", end="")
        userscore = userscore + 1
    elif (user_selection == 3 and computer_selection == 1):
        print("Computer won, Rock wins=>\n", end="")
        computerscore = computerscore + 1
    if (user_selection == 2 and computer_selection == 3):
        print("Player won, scissors win => \n", end="")
        userscore = userscore + 1
    elif (user_selection == 3 and computer_selection == 2):
        print("Computer won, scissors win => \n", end="")
        computerscore = computerscore + 1
        
    print("userscore: ", userscore)
    print("computerscore: ", computerscore)
    return userscore, computerscore
    

def main():
    """
    Run all program functions
    """
    while True:
        condition_check()
        print("Do you want to play again? (Y/N)")

        ans = input().lower()
        if ans == 'n':
            break
    print("thanks for playing")

main()