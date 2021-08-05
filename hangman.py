import random
from words import word_list

def get_word():
    # take random secret word from word_list from words file
    secret_word = random.choice(word_list)
    return secret_word.upper()

def play(secret_word):
    # variables that will be updated during the play of Hangman when player takes turns to guess the secret word
    reveal = "_" * len(secret_word)
    gameWon = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    # welcoming the player
    print("-------------------------------------------------- ")
    print("Welcome to the classic game of Hangman!")
    print("The secret word to guess is represented")
    print("by a row of underscores.")
    print("If you guess a letter which exists")
    print("in the secret word, the script writes it")
    print("in the correct position.")
    print("You have 6 lives. Best of Luck!")
    print("-------------------------------------------------- ")
    name = input("Please Enter Your Name: ")    
    print(f"Hello {name}, Let's play Hangman....")
    print("--------------------------------------------------- \n")        
    print(display_hangman(lives))
    print(f"SECRET WORD: {reveal}")
    print("\n")
    print(f"You have {lives} lives")
    print("\n")
    # code in while loop runs either until secret word is guessed or player runs out of lives
    while gameWon == False and lives > 0:
        guess = input("Guess a letter or word: ").upper()
        # if letter in alphabet is already guessed, or is not in the secret word, you lose one live
        if len(guess) == 1 and guess.isalpha():

        # if player already guessed a specific word that is not the secret word, or input is not the secret word, you lose one live.                   
        elif len(guess) == len(secret_word) and guess.isalpha():

        else:
            # if input is not a letter from alphabet or word that is not the same length of secret word
            print("Not a valid guess. Please try again!")
        print(display_hangman(lives))
        print(f"SECRET WORD: {reveal}")
        print("\n")
        print(f"You have {lives}, lives")
        print("\n")





def display_hangman(lives):
    # index of each stage that corresponts with the number of lives that the player have

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