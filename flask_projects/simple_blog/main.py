from flask import Flask, render_template
import requests
from post import Post


post_objects = []


# Get all posts
def get_all_posts():
    response = requests.get(url="https://api.npoint.io/23cc74e61161d4b00a1b", verify=False)
    response.raise_for_status()
    posts = response.json()
    for post in posts:
        post_obj = Post(post_id=post['id'], title=post['title'], subtitle=post['subtitle'], text=post['text'])
        post_objects.append(post_obj)
    return post_objects


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=get_all_posts())


# Get blog post
@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
