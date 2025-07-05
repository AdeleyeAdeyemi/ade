import random

class Guess_Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def check_guess(self, guess):
        return guess == self.secret_number
