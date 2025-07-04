from flask import Flask, request, render_template
import random

app = Flask(__name__)

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.usd_to_ils_rate = 3.7

    def get_money_interval(self, usd_amount):
        margin = 5 - self.difficulty
        return (usd_amount * self.usd_to_ils_rate - margin, usd_amount * self.usd_to_ils_rate + margin)

@app.route('/currency', methods=['GET', 'POST'])
def currency_roulette():
    if request.method == 'GET':
        # Show difficulty input
        return render_template('currency.html', step='difficulty')

    step = request.form.get('step')

    if step == 'difficulty_submit':
        # User submitted difficulty, generate USD amount and show guess form
        difficulty = request.form.get('difficulty')
        if difficulty and difficulty.isdigit():
            difficulty = int(difficulty)
            usd_amount = random.randint(1, 100)
            return render_template('currency.html', step='guess', difficulty=difficulty, usd_amount=usd_amount)
        else:
            return render_template('currency.html', step='difficulty')

    elif step == 'guess_submit':
        # User submitted guess, check it and show result
        difficulty = request.form.get('difficulty')
        usd_amount = request.form.get('usd_amount')
        guess = request.form.get('guess')

        try:
            difficulty = int(difficulty)
            usd_amount = float(usd_amount)
            guess = float(guess)
        except (ValueError, TypeError):
            return render_template('currency.html', step='difficulty')

        game = CurrencyRouletteGame(difficulty)
        interval = game.get_money_interval(usd_amount)

        if interval[0] <= guess <= interval[1]:
            message = f"Congrats! Your guess is correct. The value was between {interval[0]:.2f} and {interval[1]:.2f}."
        else:
            message = f"Sorry, wrong guess. The value was between {interval[0]:.2f} and {interval[1]:.2f}."

        return render_template('currency.html', step='result', message=message)

    else:
        # Default fallback: show difficulty input
        return render_template('currency.html', step='difficulty')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

