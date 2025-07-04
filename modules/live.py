def welcome_message(name):
    return f"Hello {name}, welcome to your World of Games!"

def print_game_options(name):
    print(f"\nPlease press one of the following options to play, {name}:")
    print("1 - Memory_Game")
    print("2 - Guess_Game")
    print("3 - Currency_Roulette")
    print("Q - Quit")

def select_level(game_name):
    print(f"\nWelcome to your {game_name}!")
    print("Please select your difficulty level:")
    for i in range(1, 6):
        print(f"Level {i}")
    while True:
        level = input("Select your level (1-5): ")
        if level in ['1', '2', '3', '4', '5']:
            print(f"Level {level} {game_name} loading...")
            return int(level)
        else:
            print("Invalid input! Please enter a number between 1 and 5.")

def main():
    name = input("Insert your name: ")
    print(welcome_message(name))

    while True:
        print_game_options(name)
        choice = input("Select a game (1/2/3) or Q to quit: ").strip().upper()

        if choice == 'Q':
            print(f"Goodbye, {name}! Thanks for playing.")
            break

        if choice not in ('1', '2', '3'):
            print("Invalid choice! Please select 1, 2, 3, or Q to quit.")
            continue

        if choice == '1':
            level = select_level("Memory_Game")
            # call your Memory_Game here

        elif choice == '2':
            level = select_level("Guess_Game")
            # call your Guess_Game here

        elif choice == '3':
            level = select_level("Currency_Roulette")
            # call your Currency_Roulette_Game here

if __name__ == "__main__":
    main()
