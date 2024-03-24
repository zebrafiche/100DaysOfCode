from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import tmdb

# Initialize the App
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db = SQLAlchemy(app)


# Create the database
class movie_list(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), unique=True, nullable=False)
   year = db.Column(db.BigInteger, nullable=False)
   description = db.Column(db.String(500), nullable=False)
   rating = db.Column(db.Float(3))
   ranking = db.Column(db.Integer, nullable=False)
   review = db.Column(db.String(1000), nullable=False)
   img_url = db.Column(db.Text, nullable=False)


# launch the app
with app.app_context():
    # create the columns
    db.create_all()
    # print(movie_list.query.all())

# add new record
# with (app.app_context()):
#     try:
#         # add new data
#         new_movie = movie_list(
#             title="Phone Booth",
#             year=2002,
#             description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#             rating=7.3,
#             ranking=10,
#             review="My favourite character was the caller.",
#             img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#         )
#         db.session.add(new_movie)
#         db.session.commit()
#     except:
#         print("Duplicate movie title encountered.")


# Homepage
@app.route("/")
def home():
    with (app.app_context()):
        all_movies = db.session.query(movie_list).order_by(movie_list.rating.desc())
        for the_movie in all_movies.all():
            the_movie.ranking = all_movies.all().index(the_movie) + 1
            db.session.commit()
    return render_template("index.html", movies_list_with_details=all_movies.all())
                           # title=all_movies[0].title,
                           # date=all_movies[0].year,
                           # rating=all_movies[0].rating,
                           # review=all_movies[0].review,
                           # overview=all_movies[0].description,
                           # rank=all_movies[0].ranking,
                           # link=all_movies[0].img_url)


# Delete Function
@app.route("/delete/<movie_name>")
def delete_movie(movie_name):
    with (app.app_context()):
        movie_to_delete = movie_list.query.filter_by(title=movie_name).first()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


# Edit Form
class MovieForm(FlaskForm):
    rating = FloatField(label='Rating', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Edit Page
@app.route("/edit/<movie_name>", methods=['GET', 'POST'])
def edit(movie_name):
    form = MovieForm()
    if form.validate_on_submit():
        with (app.app_context()):
            movie_to_update = movie_list.query.filter_by(title=movie_name).first()
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie_name_to_use=movie_name, form=form)


# Add Form
class AddForm(FlaskForm):
    title = StringField(label='Name Of The Movie', validators=[DataRequired()])
    submit = SubmitField('Search')


# Add Page
@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_query = tmdb.MovieQuery()
        movie = movie_query.search(form.title.data)
        return render_template("select.html", movie_data=movie)
    return render_template("add.html", form=form)


# Select Function
@app.route("/select/<int:movie_id>")
def select(movie_id):
    movie_query = tmdb.MovieQuery()
    movie = movie_query.search_by_id(movie_id)
    with (app.app_context()):
        # add new data
        new_movie = movie_list(
            title=movie["movie_title"],
            year=movie["movie_release_date"][:4],
            description=movie["movie_overview"],
            rating=0.0,
            ranking=0,
            review='Null',
            img_url=f"https://image.tmdb.org/t/p/w500/{movie['movie_poster']}"
        )
        db.session.add(new_movie)
        db.session.commit()
    # return redirect(url_for('home'))
    return redirect(url_for('edit', movie_name=movie["movie_title"]))


if __name__ == '__main__':
    app.run(debug=True)


