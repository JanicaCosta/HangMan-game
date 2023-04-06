# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random
import os
import time


# categories for the game and list of words

Countries_Cities = ["portugal", "spain", "france", "italy", "Iceland", "scotland", "croatia", "lisbon", "london", "rome", "paris", "porto", "madrid"]

Clubs = ["Sporting", "Benfica", "Porto", "Liverpool", "Arsenal", "Tottenham", "Barcelona", "Juventus"]

categories = [Countries_Cities, Clubs]

def reception():
    """
    introduction to the game - welcome message
    """

    print(" _      _____ _     ____  ____  _      _____  ")
    print("/ \  /|/  __// \   /   _\/  _ \/ \__/|/  __/  ")
    print("| |  |||  \  | |   |  /  | / \|| |\/|||  \    ")
    print("| |/\|||  /_ | |_/\|  \_ | \_/|| |  |||  /_   ")
    print("\_/  \|\____\\____/\____/\____/\_/  \|\____\  ")
    print("                 _____  ____                  ")
    print("                /__ __\/  _ \                 ")
    print("                  / \  | / \|                 ")
    print("                  | |  | \_/|                 ")
    print("                  \_/  \____/                 ")
    print(" _     ____  _      _____ _      ____  _      ")
    print("/ \ /|/  _ \/ \  /|/  __// \__/|/  _ \/ \  /| ")
    print("| |_||| / \|| |\ ||| |  _| |\/||| / \|| |\ || ")
    print("| | ||| |-||| | \||| |_//| |  ||| |-||| | \|| ")
    print("\_/ \|\_/ \|\_/  \|\____\\_/  \|\_/ \|\_/  \| ")

    time.sleep(5)
    os.system('cls' if os.name=='nt' else 'clear')
    name = input("Please Enter your name :")
    print(f"Hello {name}, lets start play!!!")


def game_rules():
    """This function asks the user if they know the game rules.
    If the user says no, it will display the rules.
    If the user says yes, it will pass.
    """
    # Ask the user if they know the game rules
    answer = input("Do you know the game rules? (yes/no) ")
    
    # If the user says no, display the rules
    if answer.lower() == "no":
        print("Here is instruction on how to play \n"
          "1. Choose a category\n"
          "2. The same number of Underscores '_' will be displayed \n"
          "   as letters in the word.\n"
          "3. Guess the word\n"
          "   Only one alphabet key should be entered at each time.\n"
          "   Space between the words is considered incorrect.\n"
          "4. If your answer is correct, the letter will be displayed\n"
          "   instead of the underscore'_'.\n"
          "5. If you guess all the letters and complete the word,\n"
          "   you win the game\n"
          "6. If the incorrect answer is entered,"
          " the hangman image will progress.\n"
          "7. If the number of incorrect attempts reaches the limit\n"
          "   and hangman image completes, game over!")
    # If the user says yes, pass

    elif answer.lower() == "yes":
        pass
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    time.sleep(10)
    os.system('cls' if os.name=='nt' else 'clear')


reception()
game_rules()