import random
from words import word_list


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
    reveal = "_" * len(secret_word)
    gameWon = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    # welcoming the player
    print("--------------------------------------------------")
    print("Welcome to the classic game of Hangman!")
    print("The secret word to guess is represented")
    print("by a row of underscores.")
    print("If you guess a letter which exists")
    print("in the secret word, the script writes it")
    print("in the correct position.")
    print("You have 6 lives. Best of Luck!")
    print("--------------------------------------------------")
    name = input("Please Enter Your Name: ").upper()
    print(f"Hello {name}, Let's play Hangman....")
    print("---------------------------------------------------")
    print(display_hangman(lives))
    print(f"SECRET WORD: {reveal}")
    print("\n")
    print(f"You have {lives} lives")
    print("\n")
    while not gameWon and lives > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in secret_word:
                print(f"{guess} is not in the secret word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the secret word!")
                guessed_letters.append(guess)
                word_as_list = list(reveal)
                # find all indices where guess occurs in secret word
                indices = [i for i, letter in enumerate(secret_word)
                           if letter == guess]
                # replace each underscores at index with guess
                for index in indices:
                    word_as_list[index] = guess
                reveal = "".join(word_as_list)
                if "_" not in reveal:
                    gameWon = True
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed that word, {guess}.")
            elif guess != secret_word:
                print(f"{guess} is not the secret word.")
                lives -= 1
                guessed_words.append(guess)
            else:
                gameWon = True
                reveal = secret_word
        else:
            print("Not a valid guess. Please try again!")
        print(display_hangman(lives))
        print(f"SECRET WORD: {reveal}")
        print("\n")
        print(f"You have {lives}, lives")
        print("\n")
    if gameWon:
        print(f"WELL DONE {name}, YOU ARE A CHAMPION!")
    else:
        print(f"YOU FAILED {name}! THE SECRET WORD WAS '{secret_word}'.")


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


def main():
    """
    to run game once and if want to continue or not
    """
    secret_word = get_word()
    play(secret_word)
    while input("Do You want to Play Again? (Y/N) ").upper() == "Y":
        secret_word = get_word()
        play(secret_word)


# code frame so that program will run script on command line
if __name__ == "__main__":
    main()
