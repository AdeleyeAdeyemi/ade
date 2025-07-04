from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/memory')
def memory_game():
    return render_template('memory.html')

@app.route('/guess')
def guess_game():
    return render_template('guess.html')

@app.route('/currency')
def currency_roulette():
    return render_template('currency.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

