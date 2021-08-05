import random
from words import word_list

def get_word():
    # take random secret word from word_list from words file
    secret_word = random.choice(word_list)
    return secret_word.upper()

