from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///movie.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
API_KEY = "9f0acdd8298bbad45700efa967710377"
IMAGE_HTTP = "https://image.tmdb.org/t/p/w500/"
MOVIE_URL = "https://api.themoviedb.org/3/movie/"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80), unique=True,nullable=True)
    year= db.Column(db.Integer)
    description= db.Column(db.String(80), unique=True,nullable=True)
    rating= db.Column(db.Integer)
    ranking= db.Column(db.Integer)
    review= db.Column(db.String(80), unique=True,nullable=True)
    img_url= db.Column(db.String(80), unique=True,nullable=True)

    def __repr__(self):
        return f"Movie: {self.title}"

db.create_all()

class EditAMovie(FlaskForm):
    rating=StringField(label="Your rating out of 10:")
    review= StringField(label="Your Review:")
    submit = SubmitField(label="Submit")

class AddAMovie(FlaskForm):
    add = StringField(label="Which movie would you like?:")
    submit = SubmitField(label="Add Movie")

# new_movie = Movie(
#     title="Phone Booths",
#     year=2004,
#     description="sPublicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.2,
#     ranking=3,
#     review="My favourite character was the callers.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpgs"
# )
#
# db.session.add(new_movie)
# db.session.commit()
# db.session.delete(new_movie)
# db.session.commit()

@app.route("/", methods= ["POST", "GET"])
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods= ["POST", "GET"])
def edit():
    form = EditAMovie()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit() and request.method == "POST":
        form_rating = float(form.rating.data)
        form_review = form.review.data
        movie.rating = form_rating
        movie.review = form_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form= form)

@app.route("/delete")
def delete():
    if 'sure' in request.files:
        movie_id = request.args.get("id")
        movie1 = Movie.query.get(movie_id)
        db.session.delete(movie1)
        db.session.commit()
    return render_template('sure.html')

@app.route('/add', methods=["POST", "GET"])
def add():
    form = AddAMovie()
    movie_api_id = request.args.get("id")
    if request.method == "POST":
        movie_requested = form.add.data
        print(form.add.data)
        response = requests.get(url=f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_requested}").json()
        all_selected_movies = response["results"]
        for movie in all_selected_movies:
            print(movie["original_title"])
        return render_template('select.html', movies=all_selected_movies)
    return render_template('add.html', form = form)

@app.route('/find')
def find():
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    if movie_api_id:
        movie_api_url = f"{MOVIE_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{IMAGE_HTTP}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
