import random


class GuessGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret = self.generate_number()

    def generate_number(self):
        return random.randrange(self.difficulty)

    def get_guess_from_user(self):
        return input("Please type a number from 1 to %d \n" % self.difficulty)

    def compare_results(self):
        return self.get_guess_from_user() == 0

