import os

if __name__ == "__main__":
    env = os.environ.get("ENV", "dev")

    if env == "dev":
        name = input("Insert your name: ")
    else:
        name = os.environ.get("PLAYER_NAME", "Player")

    from modules.live import welcome_message, print_game_options
    from modules.Currency_Roulette import play as currency_roulette_game
    from modules.Guess_Game import Guess_Game
    from modules.Memory_Game import Memory_Game

    print(welcome_message(name))
    print_game_options(name)
