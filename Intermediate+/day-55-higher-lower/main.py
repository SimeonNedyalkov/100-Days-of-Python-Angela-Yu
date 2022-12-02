from flask import Flask
import random


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src= https://media0.giphy.com/media/NAy2FD8xWrH4jUIBrq/200w.webp?cid=ecf05e478s0k1sxmgz6t9bguucnfl3qi6v8iall5xmskgnq6&rid=200w.webp&ct=g>'

random_number = random.randint(0,9)

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return f"<h1>{guess} is too high </h1>" \
               "<img src=https://media2.giphy.com/media/JT7Td5xRqkvHQvTdEu/200w.webp?cid=ecf05e4725l1sami7hwbpstsa6hsl0q541q0avebqazel6e6&rid=200w.webp&ct=g>"

    elif guess < random_number:
        return f"<h1>{guess} is too low </h1>" \
               "<img src=https://media2.giphy.com/media/JT7Td5xRqkvHQvTdEu/200w.webp?cid=ecf05e4725l1sami7hwbpstsa6hsl0q541q0avebqazel6e6&rid=200w.webp&ct=g>"

    elif guess == random_number:
        return f"<h1>{guess} is the correct number</h1>" \
               "<img src= https://media0.giphy.com/media/uVpPvvpU3nip5pBkPD/200w.webp?cid=ecf05e472hi9idgdjaqxiukjrvqkk9vm9blyr1vi950vroh6&rid=200w.webp&ct=g>"

if __name__ == "__main__":
    app.run(debug=True)
