from GuessGame import play as guess_game_play
from memoryGame import play as memory_game_play
from currency_roulette_game import play as currency_roulette_game_play


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
    print("Please Choose a game to play:")
    for gamenumber in games.keys():
        print(gamenumber+". "+games[gamenumber]['Title']+" - "+games[gamenumber]['Description'])
    gamesnumber = len(games.keys())
    gametoload = input()
    while not input_validation("intrange", 1, len(games.keys()), gametoload):
        gametoload = input("You have entered an invalid choice. Please Enter a choice between 1 to %s\n" % gamesnumber)
    return gametoload


def choose_level():
    gamelevel = input("Please choose game difficulty from 1 to 5:\n")
    while not input_validation("intrange", 1, 5, gamelevel):
        gamelevel = input("You have entered an invalid choice. Please Enter a choice between 1 to 5\n")
    return int(gamelevel)


def load_game():
    game = choose_game()
    level = choose_level()
    if game == '1':
        game_outcome = memory_game_play(level)
    if game == '2':
        game_outcome = guess_game_play(level)
    if game == '3':
            game_outcome = currency_roulette_game_play(level)
    if game_outcome:
        print("Success! you won the game!")
    else:
        print("Defeat! you lost the game!")

print(welcome("Guy"))
load_game()
