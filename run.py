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

reception()