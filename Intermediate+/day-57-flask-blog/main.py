from flask import Flask, render_template
from post import Post
import requests


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
all_post_objects = []
for post in all_posts:
    post = Post(post["id"], post["body"], post["title"], post["subtitle"])
    all_post_objects.append(post)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html", post=all_post_objects)

@app.route('/post/<id>')
def posts(id):
    returned_id = int(id) - 1
    print(returned_id)
    return render_template("post.html", post_id = returned_id, posts = all_post_objects[returned_id])

if __name__ == "__main__":
    app.run(debug=True)
