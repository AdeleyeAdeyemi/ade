from flask import Flask
from Utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
        return f"""
        <html>
        <head><title>Scores Game</title></head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
        <head><title>Scores Game</title></head>
        <body>
            <h1><div id="score" style="color:red">{str(e)}</div></h1>
        </body>
        </html>
        """

if __name__ == '__main__':
    port = int(os.getenv("FLASK_RUN_PORT", 8777))  # Read port from environment
    app.run(host='0.0.0.0', port=port)





