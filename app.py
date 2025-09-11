from flask import Flask, render_template, request, session, redirect, url_for
import random
import logging
import logstash
import os


# Import your game classes from modules folder
from modules.Guess_Game import Guess_Game
from modules.Memory_Game import MemoryGame
from modules.Currency_Roulette import Currency_Roulette_Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-secret-key'


ELK_HOST = os.environ.get('ELK_HOST', 'logstash')
LOGGER = logging.getLogger('python-logstash-logger')
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(logstash.TCPLogstashHandler(ELK_HOST, 5044, version=1))


# --- Home route ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Guess Game ---
@app.route('/guess', methods=['GET', 'POST'])
def guess_game():
    if request.method == 'GET':
        # Set difficulty to 20 by default or can be a param
        difficulty = 20
        game = Guess_Game(difficulty)
        game.generate_number()
        session['guess_secret_number'] = game.secret_number
        session['guess_difficulty'] = difficulty
        return render_template('guess.html', message="Guess a number between 1 and {}".format(difficulty))

    else:
        try:
            user_guess = int(request.form['guess'])
        except (ValueError, KeyError):
            return render_template('guess.html', message="Invalid input! Please enter a number.")

        secret_number = session.get('guess_secret_number')
        difficulty = session.get('guess_difficulty', 20)

        if user_guess == secret_number:
            message = "You won! The number was {}.".format(secret_number)
        else:
            message = f"Try again. The correct number was {secret_number}."

        # Clear session for next game
        session.pop('guess_secret_number', None)
        session.pop('guess_difficulty', None)

        return render_template('guess.html', message=message)

# --- Memory Game ---
@app.route('/memory', methods=['GET', 'POST'])
def memory_game():
    message = None
    game_over = False

    if request.method == 'GET':
        difficulty = 5
        game = MemoryGame(difficulty)
        game.generate_sequence()
        session['memory_sequence'] = game.sequence
        message = f"Memorize this sequence: {game.sequence}"

    else:
        user_input = request.form.get('user_sequence', '')
        try:
            user_sequence = list(map(int, user_input.strip().split()))
        except ValueError:
            message = "Invalid input! Please enter numbers separated by spaces."
            return render_template('memory.html', message=message, game_over=False)

        correct_sequence = session.get('memory_sequence', [])
        if user_sequence == correct_sequence:
            message = "Congratulations! You've remembered the sequence correctly!"
        else:
            message = f"Sorry, you lost! The correct sequence was {correct_sequence}."
        game_over = True
        session.pop('memory_sequence', None)

    return render_template('memory.html', message=message, game_over=game_over)

# --- Currency Roulette ---
@app.route('/currency', methods=['GET', 'POST'])
def currency_roulette():
    step = request.form.get('step', 'difficulty')
    error = None
    message = None

    if step == 'difficulty_submit':
        try:
            difficulty = int(request.form['difficulty'])
            if difficulty < 1 or difficulty > 5:
                raise ValueError()
            session['currency_difficulty'] = difficulty
            session['usd_amount'] = random.randint(1, 100)
            return render_template('currency.html', step='guess', usd_amount=session['usd_amount'])
        except (ValueError, KeyError):
            error = "Please enter a valid difficulty between 1 and 5."
            return render_template('currency.html', step='difficulty', error=error)

    elif step == 'guess_submit':
        try:
            difficulty = session.get('currency_difficulty')
            usd_amount = session.get('usd_amount')
            guess = float(request.form['guess'])
        except (ValueError, KeyError):
            error = "Invalid guess or session expired. Please start again."
            return render_template('currency.html', step='difficulty', error=error)

        # Use your CurrencyRouletteGame logic here
        game = Currency_Roulette_Game(difficulty)
        usd_to_ils_rate = game.get_current_usd_to_ils_rate()
        total_value = usd_amount * usd_to_ils_rate
        margin = 5 - difficulty
        interval = (total_value - margin, total_value + margin)

        if interval[0] <= guess <= interval[1]:
            message = f"Congratulations! Your guess is correct. The correct value was between {interval[0]:.2f} and {interval[1]:.2f}."
        else:
            message = f"Sorry, your guess is incorrect. The correct value was between {interval[0]:.2f} and {interval[1]:.2f}."

        # Clear session for next game
        session.pop('currency_difficulty', None)
        session.pop('usd_amount', None)

        return render_template('currency.html', step='result', message=message)

    # Default: show difficulty selection form
    return render_template('currency.html', step='difficulty')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8777, debug=False)

    












