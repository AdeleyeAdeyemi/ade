from flask import Flask, render_template, redirect, url_for
import MainGame

app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play/<game_name>')
def play_game(game_name):
    difficulty = 1  # You can later change this to allow user selection

    if game_name.lower() == "memory":
        MainGame.play_game(difficulty, "Memory Game")
    elif game_name.lower() == "guess":
        MainGame.play_game(difficulty, "Guess Game")
    elif game_name.lower() == "roulette":
        MainGame.play_game(difficulty, "Currency Roulette")
    else:
        return f"Game '{game_name}' not found.", 404

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)

