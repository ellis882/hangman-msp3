import random
from words import word_list

def get_word():
    # take random secret word from word_list from words file
    secret_word = random.choice(word_list)
    return secret_word.upper()

def play(secret_word):    
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
    # runs either until secret word is guessed or player lost lives
    while gameWon == False and lives > 0:
        guess = input("Guess a letter or word: ").upper()
        # if letter alphabet already is guessed
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            # letter not in secret word, lose one live    
            elif guess not in secret_word:
                print(f"{guess} is not in the secret word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                # list comprehension to see if guess is in secret word
                print(f"Good job, {guess} is in the secret word!")
                guessed_letters.append(guess)
                word_as_list = list(reveal)
                indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                # reveal all occurences of guess
                for index in indices:
                    word_as_list[index] = guess
                reveal = "".join(word_as_list)
                # if guessed all letters you win
                if "_" not in reveal:
                    gameWon = True    

        # statements for if word guess is wrong                   
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed that word, {guess}")
            elif guess != secret_word:
                print(f"{guess} is not the secret word.")
                lives -= 1
                guessed_words.append(guess)
            # or you guessed the secret word and win     
            else:
                gameWon = True
                reveal = secret_word    

        else:
            # input is not a letter from alphabet
            # input is not same length as secret word
            print("Not a valid guess. Please try again!")
        print(display_hangman(lives))
        print(f"SECRET WORD: {reveal}")
        print("\n")
        print(f"You have {lives}, lives")
        print("\n")
    if gameWon:
        print("WELL DONE YOU ARE A CHAMPION!")
    else:
        print(f"YOU FAILED! THE SECRET WORD WAS '{secret_word}'")    


def display_hangman(lives):
    # index stage that corresponts with the number of lives player have

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
    # to run the game once
    secret_word = get_word()
    play(secret_word)
    # to play again if you type y    
    while input("Do You want to Play Again? (Y/N) ").upper() == "Y":
        secret_word = get_word()
        play(secret_word)


# code frame so that program will run script on command line
if __name__ == "__main__":    
    main()


