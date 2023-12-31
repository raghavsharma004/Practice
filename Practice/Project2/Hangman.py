# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:24:20 2023

@author: raghav
"""

import random
from words import words
import string

#print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    user_letter = input('Guess a letter: ').upper()
    
user_input = input('Type something: ')
    

