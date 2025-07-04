from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Add secret key for session support

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.usd_to_ils_rate = 3.7

    def get_money_interval(self, usd_amount):
        margin = 5 - self.difficulty
        return (usd_amount * self.usd_to_ils_rate - margin, usd_amount * self.usd_to_ils_rate + margin)

@app.route('/currency', methods=['GET', 'POST'])
def currency_roulette():
    if request.method == 'POST':
        if 'difficulty' not in session:
            # First form submission: user sends difficulty
            try:
                difficulty = int(request.form['difficulty'])
                if not 1 <= difficulty <= 5:
                    raise ValueError()
            except ValueError:
                return render_template('currency.html', error="Enter difficulty 1-5")
            
            session['difficulty'] = difficulty
            session['usd_amount'] = random.randint(1, 100)
            return render_template('currency_guess.html', usd_amount=session['usd_amount'])
        
        else:
            # Second form submission: user sends guess
            try:
                guess = float(request.form['guess'])
            except ValueError:
                return render_template('currency_guess.html', usd_amount=session['usd_amount'], error="Invalid guess")

            game = CurrencyRouletteGame(session['difficulty'])
            interval = game.get_money_interval(session['usd_amount'])

            if interval[0] <= guess <= interval[1]:
                result = f"Congrats! Your guess was correct. The value was between {interval[0]:.2f} and {interval[1]:.2f}."
            else:
                result = f"Sorry, wrong guess. The value was between {interval[0]:.2f} and {interval[1]:.2f}."

            session.pop('difficulty')
            session.pop('usd_amount')
            return render_template('currency_result.html', result=result)
    
    # GET request: show difficulty input form and clear session
    session.pop('difficulty', None)
    session.pop('usd_amount', None)
    return render_template('currency.html')
