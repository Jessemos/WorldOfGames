# MemoryGame.py
# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.
# Properties
# 1. Difficulty
#
# Methods
# 1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
# length will be difficulty.
# 2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
# will be in the size of difficulty.
# 3. is_list_equal - A function to compare two lists if they are equal. The function will return
# True / False.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.


import random
import time
import os


def generate_sequence(difficulty):
    input("Please note - The sequence will be visible for 0.7 seconds! press Enter to continue...:")
    sequence = []
    for index in range(int(difficulty)):
        sequence.append(random.randrange(101)+1)
    print("sequence is:{}".format(sequence))
    return sequence


def get_list_from_user(difficulty):
    sequence = []
    for index in range(int(difficulty)):
        sequence.append(int(input("Please Insert a Number for place number %d in the list:\n" % (index+1))))
    return sequence


def is_list_equal(secret_sequence,user_sequence):
    return secret_sequence == user_sequence

def play(difficulty):
    secret_sequence = generate_sequence(difficulty)
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(secret_sequence,user_sequence):
        #print("Success! Secret list is %s. Your guess was: %s" % (secret_sequence, user_sequence))
        return True
    else:
        #print("Defeat! Secret list is %s. Your guess was: %s" % (secret_sequence, user_sequence))
        return False
