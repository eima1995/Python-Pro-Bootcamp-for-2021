from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
lst_posts = []
for post in posts:
    p = Post(post['id'], post['title'], post['subtitle'], post['body'])
    lst_posts.append(p)

for post in lst_posts:
    print(post.id)


@app.route('/')
def home():
    return render_template("index.html", posts=lst_posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in lst_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
