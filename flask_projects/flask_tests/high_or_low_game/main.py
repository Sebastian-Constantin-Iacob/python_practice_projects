from flask import Flask
from func import *

secret_number = get_secret_number()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           '<img src="{https://giphy.com/clips/joolstv-jools-tv-1-2-3-song-counting-4pqm16XH2rQopZrdFU}">'


if __name__ == "__main__":
    app.run(debug=True)
