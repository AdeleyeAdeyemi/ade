import random

class Guess_Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        guess = None
        while guess is None:
            try:
                guess = int(input(f"Please guess a number between 1 and {self.difficulty}: "))
                if not (1 <= guess <= self.difficulty):
                    print(f"Invalid input! Enter a number between 1 and {self.difficulty}.")
                    guess = None
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        return guess

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        self.generate_number()
        guess = self.get_guess_from_user()
        if self.compare_results(guess):
            print("Congratulations! You've guessed the correct number!")
            return True
        else:
            print(f"Sorry, you lost! The correct number was {self.secret_number}.")
            return False
if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level (1-50): "))
    game = Guess_Game(difficulty)
    game.play()


