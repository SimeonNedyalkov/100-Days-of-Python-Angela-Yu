from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

all_books = []

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'




@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books= all_books)


@app.route("/add", methods= ["GET","POST"])
def add():
    if request.method == "POST":
        dict = {
            "title": request.form["book_name"],
            "author": request.form["book_author"],
            "rating": request.form["rating"]
        }
        all_books.append(dict)
        return redirect(url_for('add'))
    return render_template('add.html', len_of_list= len(all_books), all_books=all_books)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)

