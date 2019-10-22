# CurrencyRouletteGame.py
# This game will use t he free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
#
# Properties
# 1. Difficulty
# Methods
# 1. get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))
#
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.


import random
import requests

def get_exchange_rate():
    request = requests.get('https://api.exchangeratesapi.io/latest?base=USD&symbols=ILS,USD')
    rates = request.json()
    new_rate = round(float(rates["rates"]["ILS"]),3)
    return new_rate


def get_money_interval(difficulty):
    t = random.randrange(100)+1
    rate = get_exchange_rate()
    total = t * rate
    print("Total amount of dollars is %s." % t)
    interval = []
    interval.append(total-(5-difficulty))
    interval.append(total+(5-difficulty))
    return interval


def get_guess_from_user():
    return int(input("Please Type your guess of how much NIS its worth:"))

def play(difficulty):
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user()
    if (guess >= interval[0] and guess <= interval[1]):
        return True
    else:
        return False

