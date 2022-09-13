from flask import Flask, render_template
import post

all_posts = post

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
