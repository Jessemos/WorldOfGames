

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
            'Title': 'Weather Roulette',
            'Description': 'Guess the current temperature in Jerusalem.'
            }
        }
    print("Please Choose a game to play:")
    for gamenumber in games.keys():
        print(gamenumber+". "+games[gamenumber]['Title']+" - "+games[gamenumber]['Description'])
    gamesnumber= len(games.keys())
    print("\n")
    gametoload = input()
    while not input_validation("intrange", 1, len(games.keys()), gametoload):
        gametoload = input("You have entered an invalid choice. Please Enter a choice between 1 to %s\n" % gamesnumber)
    return gametoload


def choose_level():
    gamelevel = input("Please choose game difficulty from 1 to 5:\n")
    while not input_validation("intrange", 1, 5, gamelevel):
        gamelevel = input("You have entered an invalid choice. Please Enter a choice between 1 to 5\n")
    return gamelevel


def load_game():
    gametoload = choose_game()
    gamelevel = choose_level()
