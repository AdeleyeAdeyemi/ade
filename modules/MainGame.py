from modules.live import welcome_message, print_game_options
from .Currency_Roulette import play as currency_roulette_game
from .Guess_Game import Guess_Game
from .Memory_Game import Memory_Game

name = input("Insert your name: ")
print(welcome_message(name))
print_game_options(name)
