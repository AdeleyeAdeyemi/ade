from flask import Flask, request, render_template, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure random key

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.usd_to_ils_rate = 3.7

    def get_money_interval(self, usd_amount):
        margin = 5 - self.difficulty
        return (
            usd_amount * self.usd_to_ils_rate - margin,
            usd_amount * self.usd_to_ils_rate + margin
        )

@app.route('/currency', methods=['GET', 'POST'])
def currency_roulette():
    if request.method == 'POST':
        step = request.form.get('step')

        if step == 'difficulty_submit':
            difficulty = request.form.get('difficulty')
            if difficulty and difficulty.isdigit():
                difficulty = int(difficulty)
                if 1 <= difficulty <= 5:
                    usd_amount = random.randint(1, 100)
                    session['difficulty'] = difficulty
                    session['usd_amount'] = usd_amount
                    return redirect(url_for('currency_roulette'))
            return render_template('currency.html', step='difficulty', error='Please enter a number from 1 to 5.')

        elif step == 'guess_submit':
            try:
                difficulty = int(session.get('difficulty'))
                usd_amount = float(session.get('usd_amount'))
                guess = float(request.form.get('guess'))
            except (TypeError, ValueError):
                return redirect(url_for('currency_roulette'))

            game = CurrencyRouletteGame(difficulty)
            low, high = game.get_money_interval(usd_amount)

            if low <= guess <= high:
                message = f"🎉 Congrats! Your guess is correct. The value was between {low:.2f} and {high:.2f} ILS."
            else:
                message = f"❌ Sorry, wrong guess. The correct value was between {low:.2f} and {high:.2f} ILS."

            return render_template('currency.html', step='result', message=message)

    # GET request or after POST redirects
    if 'difficulty' in session and 'usd_amount' in session:
        return render_template('currency.html', step='guess',
                               difficulty=session['difficulty'],
                               usd_amount=session['usd_amount'])

    return render_template('currency.html', step='difficulty')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
