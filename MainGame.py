from GuessGame import play as guess_game_play
from memoryGame import play as memory_game_play
from currency_roulette_game import play as currency_roulette_game_play
# from Utils import screen_cleaner as screen_cleaner
from Scores import *


def input_validation(validationmethod, firsvalidator, secondvalidator, evaluatee):
    if validationmethod == "intrange":
        # check if evaluatee is integer
        try:
            isintcheck = int(evaluatee)
        except ValueError:
            return False
        return int(evaluatee) >= int(firsvalidator) and int(evaluatee) <= secondvalidator
    return False


def welcome(name):
    return str('Hello %s and welcome to the World of Games (WOG).\nHere you can find many cool games to play' % name)


def choose_game():
    games = {'1': {
            'Title': 'Memory Game',
            'Description': 'a sequence of numbers will appear for 1 second and you have to guess it back.'
           },
           '2': {
            'Title': 'Guess Game',
            'Description': 'guess a number and see if you chose like the computer.'
           },
           '3': {
            'Title': 'Currency Roulette',
            'Description': 'Try and guess the value of random amount of USD in ILS.'
            }
        }
    number_of_games = len(games.keys())
    print("Please Choose a game to play - \nEnter a choice between 1 to %s or 0 to quit:" % number_of_games)
    for game_number in games.keys():
        print(game_number+". "+games[game_number]['Title']+" - "+games[game_number]['Description'])
    game_to_load = input()
    while not input_validation("intrange", 0, number_of_games, game_to_load):
        game_to_load = input("You have entered an invalid choice. Please Enter a choice between 1 to %s\n or 0 to quit" % number_of_games)
    return game_to_load


def choose_level():
    game_level = input("Please choose game difficulty from 1 to 5:\n")
    while not input_validation("intrange", 1, 5, game_level):
        game_level = input("You have entered an invalid choice. Please Enter a choice between 1 to 5\n")
    return int(game_level)


def load_game():
    game = choose_game()
    if not game == '0':
        level = choose_level()
        if game == '1':
            game_outcome = memory_game_play(level)
        if game == '2':
            game_outcome = guess_game_play(level)
        if game == '3':
                game_outcome = currency_roulette_game_play(level)
        if game_outcome:
            print("Success! you won the game!")
            add_score(level)
        else:
            print("Defeat! you lost the game!")
            screen_cleaner()
            load_game()
    else:
        screen_cleaner()
        print("Screen cleared!")
        print("quitting!")


screen_cleaner()
print(welcome("Guy"))
load_game()
