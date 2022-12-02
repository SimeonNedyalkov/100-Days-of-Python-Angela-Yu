from flask import Flask, render_template,request
import requests
from post import Post
import smtplib

app = Flask(__name__)
response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
all_items = response.json()

list_of_items = []
for post in all_items:
    post = Post(post["id"], post["body"], post["title"], post["subtitle"])
    list_of_items.append(post)

@app.route('/')
def home():
    return render_template('index.html', posts = list_of_items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_massage = True
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user= "simeonpythontest@gmail.com", password="password")
        connection.sendmail(from_addr=email, to_addrs="simeonpythontest@gmail.com", msg=message)
        return render_template('contact.html', send_massage=send_massage)
    return render_template('contact.html', send_massage=False)

@app.route('/post/<id>')
def post(id):
    returned_id = int(id) - 1
    print(list_of_items[returned_id])
    return render_template('post.html', post = list_of_items[returned_id])



if __name__ == '__main__':
    app.run(debug=True)
