# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random
import os
import time


# categories for the game and list of words

Countries_Cities = ["portugal", "spain", "france", "italy", "Iceland", "scotland", "croatia", "lisbon", "london", "rome", "paris", "porto", "madrid"]

Clubs = ["Sporting", "Benfica", "Porto", "Liverpool", "Arsenal", "Tottenham", "barcelona", "Juventus"]

categories = [Countries_Cities, Clubs]

def reception():
    """
    introduction to the game - welcome message
    """

    print(" _      _____ _     ____  ____  _      _____  ")
    print("/ \  /|/  __// \   /   _\/  _ \/ \__/|/  __/  ")
    print("| |  |||  \  | |   |  /  | / \|| |\/|||  \    ")
    print("| |/\|||  /_ | |_/\|  \_ | \_/|| |  |||  /_   ")
    print("\_/  \|\____\\____/\____/\____/ \_/  \|\____\  ")
    print("                 _____  ____                  ")
    print("                /__ __\/  _ \                 ")
    print("                  / \  | / \|                 ")
    print("                  | |  | \_/|                 ")
    print("                  \_/  \____/                 ")
    print(" _     ____  _      _____ _      ____  _      ")
    print("/ \ /|/  _ \/ \  /|/  __// \__/|/  _ \/ \  /| ")
    print("| |_||| / \|| |\ ||| |  _| |\/||| / \|| |\ || ")
    print("| | ||| |-||| | \||| |_//| |  ||| |-||| | \|| ")
    print("\_/ \|\_/ \|\_/  \|\____\ \_/  \|\_/ \|\_/  \| ")

    time.sleep(5)
    os.system('cls' if os.name=='nt' else 'clear')
    name = input("Please Enter your name :")
    print(f"Hello {name}, lets start play!!!\n")


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
        time.sleep(3)
        os.system('cls' if os.name=='nt' else 'clear')

    else:
        print("Invalid input. Please enter 'yes' or 'no'.\n")
        return game_rules()
        time.sleep(10)
        os.system('cls' if os.name=='nt' else 'clear')


def choose_category():
    """
    Player to choose a category for the word
    """
    print("Choose a category for the word:\n")
    print("1. Countries and Cities")
    print("2. Football clubs")
    category_choice = input("Enter the number of your choice:\n")
    if category_choice == "1":
        return ["portugal", "spain", "france", "italy", "Iceland", "scotland", "croatia", "lisbon", "london", "rome", "paris", "porto", "madrid"]
    elif category_choice == "2":
        return ["Sporting", "Benfica", "Porto", "Liverpool", "Arsenal", "Tottenham", "barcelona", "Juventus"]
    else:
        print("Invalid choice. You need to ,chose only 1 or 2, Please try again.\n")
        return choose_category()


def select_word(category_words):
    """
    Random word selection from the list and display _ for each letter
    """
    # Select a random word from the list
    word = random.choice(category_words)

    # Create a list of underscores to represent the letters of the word
    word_display = ["_"] * len(word)

    return word, word_display

def restart_game():
    """
    Asks the user if they want to play again or quit.
    If the user wants to play again, calls the main() function to start a new game.
    If the user wants to quit, exits the program.
    """
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            main()
        elif play_again.lower() == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.\n")

def main():
    reception()
    game_rules()
    category_words = choose_category()
    word, word_display = select_word(category_words)
    incorrect_guesses = []

    hangman = [
        "______",
        "|    |",
        "|    ",
        "|    ",
        "|    ",
        "|    "
    ]

    # Loop until the word is guessed or the hangman is completed
    while True:
        # Display the current state of the hangman
        print("\n".join(hangman))

        # Display the current state of the word
        print(" ".join(word_display))

        # Ask the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in incorrect_guesses or guess in word_display:
            print("You already guessed that letter. Try again.")
            continue

        # Check if the guess is correct
        if guess in word:
            # Update the word display with the guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess

            # Check if the word has been completely guessed
            if "_" not in word_display:
                print("Congratulations! You guessed the word.")
                break
        else:
            # Add the incorrect guess to the list of incorrect guesses
            incorrect_guesses.append(guess)

            # Update the hangman
            if len(incorrect_guesses) == 1:
                hangman[2] = "|    O"
            elif len(incorrect_guesses) == 2:
                hangman[3] = "|    |"
            elif len(incorrect_guesses) == 3:
                hangman[3] = r"|   \|"
            elif len(incorrect_guesses) == 4:
                hangman[3] = r"|   \|/"
            elif len(incorrect_guesses) == 5:
                hangman[4] = r"|    |"
            elif len(incorrect_guesses) == 6:
                hangman[5] = r"|   /"
            
            elif len(incorrect_guesses) == 7:
                hangman[5] = r"|   / \ "

                print("\n".join(hangman))
                print(f"Game over! The word was {word}.")
                break
    restart_game()
            

main()