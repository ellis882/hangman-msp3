# Classic game of HANGMAN

The classic game of Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

![Hangman](i-am-responsive/i-am-responsive.png)


Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter or a word at a time.
After a certain number of incorrect guesses, the game ends and the player loses.
The game also ends if the player correctly identifies all the letters of the missing word.

The live version of my project is [Here]().

---

## 1. How To Play

Hangman is a paper and pencil guessing game for two or more players. If you want you can read more about it on [wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

In this version the player has to quess the secret word that is randomly picked from a word list.

The secret word is represented by a row of underscores.

You are asked to guess a letter and you have 6 lives.

If you guess a letter or word that is in the secret word the letter will be revealed.

If you guess a letter or word that is not in the secret word you lose 1 live.

The graphics of the hangman corresponts with the number of lives the player have.

You win if you can guess the secret word before the hangman is complete.

---

## 2. Features

- accepts a user's input
- performs a task based on the input
- displays the result in some useful form

### 2.1. Existing features

- takes random secret word from word list.
    - length of secret word is revealed with underscores.

- you are asked to guess a letter or word.
    - guess is being revealed when letter or word is correct.
    - wrong letter or word is showed and substracts a live.

- number of lives you see in text and graphics.
    - the text line update how many lives you have left.
    - the graphics update bodyparts(head, torso, both arms, and both legs) until hangman is complete.

- if you guess the secret word you win

- if you run out of lives you lose

- input validation and error-checking.
    - you cannot enter the same guess twice.
    - you cannot enter input that is not a letter or word of correct length of secret word.

- at the end of the game you are asked to play again? (Y/N).
    - if type Y the game starts again.
    - when type N you go to welcome text.
    - when type anything else you are asked to type only (Y/N).

### 2.2. Features left to implement in the future 

- When take out the graphics of the hangman you could increase the number of chances.

---

## 3. Data Model

- I had created a [flowchart](flowchart-hangman/hangman-program-flowchart.png) to visualize which steps to take before building   the  game. 
  This gives you a clear view on where to put the different options in your code.
  It shows a series of steps as boxes connected with arrows. Each box represents a step and the arrows show the possible next
  step(s). You can only move from one box to another in the direction of the arrow. You can never go backwards unless there's an arrow going back.

- In the code you will find 6 functions.
  The first function is the welcome text and is just printed text. You will come back there when you don't want to play again.
  The ask_name function is created to enter a name. It only accepts letters from the alphabet, no numbers.
  The get_word function pulls out a (secret)word from the list that is stored in a words file.
  This contains all the words which can be chosen from randomly by the computer.
  The display_hangman funtion is to display the hangman graphics.
  These function will come back in the play function.
  For this function i created a while loop to run the game until the secret word is guessed
  or the player runs out of lives.
  It also contains three possible conditions each based on different input.
  Guessing a letter or word or input that is not a letter or word of the
  same length as the secret word.
  After that i made a main function to run the game and put in the option to play again or not.

---

## 4. Testing

- I have tested this project by doing the following:

    - passed the code through a [PEP8](http://pep8online.com/checkresult) linter.
    - testing with invalid inputs like guessing the same letter and word twice, put a number instead of a letter.
    - tested in my local terminal and the Code Institute Heroku terminal.

### 4.1. Bugs

#### Solved Bugs

- I was getting errors of trailing whitespaces and that some lines were too long.
    - got rid of the whitespace manualy and made the text shorter.
- In order to put more input validation checking for enter your name(just letters)
 and if you want to play again or not(you can either choose Y or N) i had add the ask_name functio
 and had made a while loop in the main function for input validation checking.   

#### Remaining Bugs

- no remaining bugs

#### Validator Testing

- PEP8
    - no errors found [pep8 linter](pep8-linter/pep8-linter.png)

---

## Deployment

- This project was deployed using Code Institute's mock terminal for Heroku.

    - Steps for deployment:
        - Fork or clone this repository.
        - Create a new Heroku app.
        - Set the buildpacks to Python and NodeJS in that order.
        - Link the Heroku app to the repository.
        - Click on [Deploy]().

---

## Credits

- Code Institute for the deployment terminal.
- YouTube tutorials [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w&t=191s) and [FreeCodeCamp.org](https://www.youtube.com/watch?v=8ext9G7xspg).
- flowchart [Inventwithpython.com](https://inventwithpython.com/invent4thed/chapter7.html).


