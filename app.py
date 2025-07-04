from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('menu', player_name=name))
    return '''
        <h1>Welcome to World of Games!</h1>
        <form method="post">
            Enter your name: <input type="text" name="name" required>
            <input type="submit" value="Start">
        </form>
    '''

@app.route('/menu')
def menu():
    name = request.args.get('player_name')
    return f'''
        <h2>Hello {name}, please select a game:</h2>
        <ul>
            <li><a href="{url_for('play_game', game='memory', player_name=name)}">Memory Game</a></li>
            <li><a href="{url_for('play_game', game='guess', player_name=name)}">Guess Game</a></li>
            <li><a href="{url_for('play_game', game='currency', player_name=name)}">Currency Roulette</a></li>
        </ul>
    '''

@app.route('/play/<game>', methods=['GET', 'POST'])
def play_game(game):
    name = request.args.get('player_name')
    # Here you should add your actual game logic or forms to interact with users
    return f"<h3>Game {game.capitalize()} loading for {name}...</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
