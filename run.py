import random
from words import word_list
import os


# Funtion to clear te terminal
def clear():
    os.system("clear")


def welcome():
    # ask for players name
    print()
    print("Welcome To The Classic Game Of Hangman!")
    while True:
        name = input("Enter Your Name: \n").upper()
        if name.isalpha():
            print("----------------------------------------------")
            print(f"Hi {name}! Glad to have you here!")
            print("The secret word to guess is represented")
            print("by a row of dashes. If you guess a letter")
            print("which exists in the secret word,")
            print("the script writes it in the correct position.")
            print("You have 6 lives. Best of Luck!")
            print("----------------------------------------------")
            return name
        else:
            print("Please Use Only Letters, Try Again ")


def get_word():
    """
    take random secret word from word_list
    imported from words file
    """
    secret_word = random.choice(word_list)
    return secret_word.upper()


def play(secret_word):
    """
    create while loop to run the game until the secret word is guessed
    or player runs out of lives.
    Also contains three possible conditions each based on different input.
    Guessing a letter, word or input that is not a letter or word of
    same length as secret word.
    """
    reveal = "-" * len(secret_word)
    gameWon = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print("----------------------------------------------")
    print("Let's Play Hangman!")
    print("----------------------------------------------")
    print(display_hangman(lives))
    print(f"SECRET WORD: {reveal}")
    print("\n")
    print(f"You Have {lives} Lives")
    print("\n")
    while not gameWon and lives > 0:
        guess = input("Guess A Letter Or Word: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You Already Guessed The Letter {guess}.")
            elif guess not in secret_word:
                print(f"{guess} Is Not In The Secret Word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good Job, {guess} Is In The Secret Word!")
                guessed_letters.append(guess)
                word_as_list = list(reveal)
                # find all indices where guess occurs in secret word
                indices = [i for i, letter in enumerate(secret_word)
                           if letter == guess]
                # replace each underscores at index with guess
                for index in indices:
                    word_as_list[index] = guess
                reveal = "".join(word_as_list)
                if "-" not in reveal:
                    gameWon = True
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You Already Guessed That Word, {guess}.")
            elif guess != secret_word:
                print(f"{guess} Is Not The Secret Word.")
                lives -= 1
                guessed_words.append(guess)
            else:
                gameWon = True
                reveal = secret_word
        else:
            print("Not A Valid Guess. Please Try Again!")
        print(display_hangman(lives))
        print(f"SECRET WORD: {reveal}")
        print("\n")
        print(f"You Have {lives}, Lives Left")
        print("\n")
    if gameWon:
        print("WELL DONE, YOU ARE A CHAMPION!")
    else:
        print(f"YOU FAILED! THE SECRET WORD WAS '{secret_word}'.")


def display_hangman(lives):
    """
    index stage that corresponts with the number of lives player have
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[lives]


# code frame so that program will run script on command line
if __name__ == "__main__":
    clear()

    # Types of categories
    topics = {1: "Start Game", 2: "Play Again"}

    # The GAME LOOP
    while True:

        # Printing the game menu
        print()
        print("----------------------------------------------")
        print("\t\tGAME MENU")
        print("----------------------------------------------")
        for key in topics:
            print("Press", key, "to", topics[key])
        print("Press", len(topics)+1, "to Quit")
        print()

        # Handling the player category choice
        try:
            choice = int(input("Enter Your Choice = \n"))
        except ValueError:
            clear()
            print("Invalid Choice!!! Try Again")
            continue

        # Sanity checks for input
        if choice > len(topics)+1:
            clear()
            print("Not An Option!!! Try Again.")
            continue

        # The EXIT choice
        elif choice == len(topics)+1:
            print()
            print("Thank You For Playing!")
            break

        # The topic chosen
        chosen_topic = topics[choice]

        if chosen_topic == "Start Game":
            welcome()
            secret_word = get_word()
            play(secret_word)
        if chosen_topic == "Play Again":
            secret_word = get_word()
            play(secret_word)
