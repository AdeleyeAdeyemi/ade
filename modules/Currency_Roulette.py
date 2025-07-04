import random

class Currency_Roulette_Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.usd_to_ils_rate = None
        
    def get_money_interval(self, usd_amount):
        self.usd_to_ils_rate = self.get_current_usd_to_ils_rate()
        total_value = usd_amount * self.usd_to_ils_rate

        margin = 5 - self.difficulty
        interval = (total_value - margin, total_value + margin)
        return interval

    def get_current_usd_to_ils_rate(self):
        # For simplicity, this is a static rate
        return 3.7

    def get_guess_from_user(self, usd_amount):
        while True:
            try:
                guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
                return guess
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def play(self):
        usd_amount = random.randint(1, 100)
        interval = self.get_money_interval(usd_amount)
        guess = self.get_guess_from_user(usd_amount)

        if interval[0] <= guess <= interval[1]:
            print(f"Congratulations! Your guess is correct. The correct value was between {interval[0]:.2f} and {interval[1]:.2f}.")
            return True
        else:
            print(f"Sorry, your guess is incorrect. The correct value was between {interval[0]:.2f} and {interval[1]:.2f}.")
            return False


def play(difficulty):
    game = Currency_Roulette_Game(difficulty)
    return game.play()


if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level (1-5): "))
    play(difficulty)
