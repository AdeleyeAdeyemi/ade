from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/guess', methods=['GET', 'POST'])
def play_guess():
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        answer = session.get('answer', 10)
        if user_guess == answer:
            message = "You won!"
            session.pop('answer', None)
        else:
            message = "Try again."
        return render_template('guess.html', message=message)
    else:
        # Start new game
        import random
        session['answer'] = random.randint(1, 20)
        return render_template('guess.html', message="Guess a number between 1 and 20.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
