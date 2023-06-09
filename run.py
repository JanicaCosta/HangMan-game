# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random
import os
import time

# Define a class named textcolor that contains
# a set of color codes for style text


class TextColor:
    PURPLE = '\033[95m'  # purple color
    RED = '\033[91m'     # red color
    YELLOW = '\033[93m'  # yellow color
    CYAN = '\033[96m'    # cyan color
    GREEN = '\033[92m'   # green color
    BOLD = '\33[1m'      # bold text
    ITALIC = '\33[3m'    # italicized text
    REDBG = '\33[41m'    # red background
    GREENBG = '\33[42m'   # green background
    BLUEBG = '\33[44m'   # blue background
    UNDERLINE = '\033[4m'  # underlined text

    ENDC = '\33[0m'  # reset to default color


# categories for the game and list of words


Countries_Cities = ["portugal",
                    "spain",
                    "france",
                    "italy",
                    "Iceland",
                    "scotland",
                    "croatia",
                    "lisbon",
                    "london",
                    "rome",
                    "paris",
                    "porto",
                    "madrid"]

Clubs = ["sporting",
         "benfica",
         "porto",
         "liverpool",
         "arsenal",
         "tottenham",
         "barcelona",
         "Juventus"]

categories = [Countries_Cities, Clubs]


def clear_screen():
    """
    this function is to clear the screen after 5 seconds
    """

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')


def reception():
    """
    introduction to the game - welcome message
    """

    print("██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ ")
    print("██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ ")
    print("███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ ")
    print("██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██")
    print("██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ ")
    clear_screen()


def get_valid_name():
    """
    register a name but with few rules,
    no numbers or lenght more then 8 letters
    """

    while True:
        name = input("Please enter your name (max 8 letters, no numbers): \n")
        if len(name) > 8:
            print("Name must be 8 letters or fewer.\n")
        elif any(char.isdigit() for char in name):
            print("Name cannot contain numbers.\n")
        else:
            print(f"Hello {name}, lets start play!!!")
            return name


def game_rules():
    """This function asks the user if they know the game rules.
    If the user says no, it will display the rules.
    If the user says yes, it will pass.
    """
    try:
        # Ask the user if they know the game rules
        answer = input("Do you know the game rules? (yes/no) ")

        # If the user says no, display the rules
        if answer.lower() == "no":
            print("Here are the instructions on how to play:\n"
                  "1. Choose a category\n"
                  "2. The same number of underscores '_' will be displayed\n"
                  "   as letters in the word.\n"
                  "3. Guess the word\n"
                  "   Only one alphabet key should be entered at a time.\n"
                  "   Space between the words is considered incorrect.\n"
                  "4. If your answer is correct, the letter will be displayed"
                  "\n"
                  "   instead of the underscore '_'.\n"
                  "5. If you guess all the letters and complete the word,\n"
                  "   you win the game.\n"
                  "6. If an incorrect answer is entered,\n"
                  "   the hangman image will progress.\n"
                  "7. If the number of incorrect attempts reaches the limit\n"
                  "   and the hangman image completes, it's game over!")

            clear_screen()

        # If the user says yes, pass
        elif answer.lower() == "yes":
            clear_screen()

        # If the user enters an invalid input
        else:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

    except ValueError as e:
        print(TextColor.REDBG + "Error:", str(e) + TextColor.ENDC, "\n")
        return game_rules()


def choose_category():
    """
    Player to choose a category for the word
    """
    try:
        print("Choose a category for the word:\n")
        print("1. Countries and Cities")
        print("2. Football clubs")
        category_choice = input("Enter the number of your choice:\n")
        if category_choice == "1":
            return ["portugal", "spain", "france", "italy", "Iceland",
                    "scotland", "croatia", "lisbon", "london", "rome",
                    "paris", "porto", "madrid"]
        elif category_choice == "2":
            return ["Sporting", "Benfica", "Porto", "Liverpool", "Arsenal",
                    "Tottenham", "barcelona", "Juventus"]
        else:
            raise ValueError("Invalid choice. Please enter either 1 or 2.\n")
    except ValueError as e:
        print(TextColor.REDBG + "Error:", str(e) + TextColor.ENDC, "\n")
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
    If the user wants to play again, calls the main() function to
    start a new game.
    If the user wants to quit, exits the program.
    """
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            play_game()
        elif play_again.lower() == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.\n")


def draw_hangman(num_incorrect_guesses):
    hangman = [
        "______",
        "|    |",
        "|    ",
        "|    ",
        "|    ",
        "|    "
    ]

    if num_incorrect_guesses >= 1:
        hangman[2] = "|    O"

    if num_incorrect_guesses >= 2:
        hangman[3] = "|    |"

    if num_incorrect_guesses >= 3:
        hangman[3] = r"|   \|"

    if num_incorrect_guesses >= 4:
        hangman[3] = r"|   \|/"

    if num_incorrect_guesses >= 5:
        hangman[4] = r"|    |"

    if num_incorrect_guesses >= 6:
        hangman[5] = r"|   /"

    if num_incorrect_guesses >= 7:
        hangman[5] = r"|   / \ "

    return "\n".join(hangman)


def play_game():
    reception()
    get_valid_name()
    game_rules()
    category_words = choose_category()
    word, word_display = select_word(category_words)
    incorrect_guesses = []
    hangman_str = draw_hangman(len(incorrect_guesses))

    # Loop until the word is guessed or the hangman is completed
    while True:
        # Display the current state of the hangman
        print(hangman_str)

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
                print("Congratulations! You won.")
                break
        else:
            # Add the incorrect guess to the list of incorrect guesses
            incorrect_guesses.append(guess)

            # Update the hangman
            hangman_str = draw_hangman(len(incorrect_guesses))

            # Check if the game is over
            if len(incorrect_guesses) == 7:
                print(hangman_str)
                print(f"Game over! The word was {word}.")
                break
    restart_game()


play_game()
