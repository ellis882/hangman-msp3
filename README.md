# Classic game of HANGMAN

The classic game of Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time.
After a certain number of incorrect guesses, the game ends and the player loses.
The game also ends if the player correctly identifies all the letters of the missing word.

The live version of my project is [Here]()

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

### 2.1. Existing features

- random secret word from word list.
    - length of secret word is revealed with underscores.

- you are asked to guess a letter or word.

- number of lives you see in text and graphics.
    - the text line update how many lives you have left.
    - the graphics add bodyparts(head, torso, both arms, and both legs) until hangman is complete.

- input validation and error-checking.
    - you cannot enter the same guess twice.
    - you cannot enter input that is not a letter or word of correct length of secret word.

- at the end of the game you are asked to play again? (Y/N).