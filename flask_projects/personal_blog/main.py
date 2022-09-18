from flask import Flask, render_template
import requests
import datetime
from post import Post

app = Flask(__name__)
post_obj = []


def get_posts():
    response = requests.get(url="https://api.npoint.io/c623ef892d16ec605190", verify=False)
    response.raise_for_status()
    post_collection = response.json()
    for post in post_collection:
        post['date'] = datetime.datetime.strptime(post['date'], '%Y%m%d').strftime('%d / %m / %Y')
        post_o = Post(post_id=post['post_id'], title=post['title'], subtitle=post['subtitle'], author=post['author'],
                      date=post['date'], post_text=post['post_text'])
        post_obj.append(post_o)
    return post_obj


@app.route('/')
def home():
    return render_template('index.html', post_list=get_posts())


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:numx>')
def get_post(numx):
    requested_post = None
    for post in post_obj:
        if int(post.p_id) == numx:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
