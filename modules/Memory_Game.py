import random
import time

class Memory_Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        user_sequence = []
        print(f"Please enter {self.difficulty} numbers one by one.")
        for i in range(self.difficulty):
            while True:
                try:
                    num = int(input(f"Number {i + 1}: "))
                    user_sequence.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        return user_sequence

    def is_list_equal(self, user_sequence):
        return self.sequence == user_sequence

    def play(self):
        self.generate_sequence()
        print("Remember the following sequence:")
        print(self.sequence)
        time.sleep(0.7)
        print("\033[H\033[J")  # Clear screen

        user_sequence = self.get_list_from_user()
        if self.is_list_equal(user_sequence):
            print("Congratulations! You've remembered the sequence correctly!")
            return True
        else:
            print(f"Sorry, you lost! The correct sequence was {self.sequence}.")
            return False

def play(difficulty):
    game = Memory_Game(difficulty)
    return game.play()

if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level (1-10): "))
    play(difficulty)
