from games.memory_game import play as play_memory
from games.guess_game import play as play_guess
from games.currency_roulette_game import play as play_currency


def welcome_message():
    try:
        name = input("Insert your name: ")
        print(f"Hi {name}, welcome to the World of Games (WoG).")
        print("Here you can find many cool games to play.")
    except EOFError:
        print("\nInput interrupted. Exiting.")
        exit(1)


def print_game_options():
    print("\nPlease choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - guess the value of a random amount of USD in ILS.\n")


def select_level(game_name):
    while True:
        try:
            level = int(input(f"Select difficulty level for {game_name} (1-5): "))
            if 1 <= level <= 5:
                return level
            else:
                print("Invalid level. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


def main():
    welcome_message()

    game_names = {
        '1': 'Memory Game',
        '2': 'Guess Game',
        '3': 'Currency Roulette'
    }

    while True:
        print_game_options()
        choice = input("Enter the number of the game you want to play (1-3): ")

        if choice in game_names:
            game_name = game_names[choice]
            level = select_level(game_name)

            print(f"\nStarting {game_name} at difficulty level {level}...\n")

            if choice == '1':
                play_memory(level)
            elif choice == '2':
                play_guess(level)
            elif choice == '3':
                play_currency(level)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

        again = input("\nDo you want to play another game? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == '__main__':
    main()

