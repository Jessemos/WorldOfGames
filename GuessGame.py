# Methods
# 1. generate_number - Will generate number between 1 to difficulty and save it to
# secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
# return the number.
# 3. compare_results - Will compare the the secret generated number to the one prompted
# by the get_guess_from_user.
#4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.

import random

#1
def generate_number(difficulty):
    return random.randrange(difficulty)+1


def get_guess_from_user(difficulty):
    return int(input("Please Insert a Number between 1 to %s:" % difficulty))


def compare_results(secret_number,difficulty):
    return secret_number == get_guess_from_user(difficulty)


def play(difficulty):
    secret_number = generate_number(difficulty)
    if (compare_results(secret_number, difficulty)):
        return True
    else:
        return False



