### 534 Day 64 Goals_ What We'll Build

We're going to build a website that compile lists of our top favourite movies of all time. 
We will be using Flask/WTForms/SQLite/SQLAlchemy and more. 
It will allow us to create a beautiful website that lists our top 10 films of all time. 
As we watch more movies, we can always update our list and keep track of which movies to recommend people.

![01](./images/01.gif)

### 535 Download the Starting Project

### 536 Requirement 1 - Be Able to View Movie List Items

This is what you're aiming for when you visit the home page:

![02](./images/02.gif)

Steps - 

1. Create an SQLite database with SQLAlchemy. 
The database needs to contain a "Movie" Table.  This table should contain the following fields:

```text
id 
title 
year 
description 
rating 
ranking
review
img_url
```

2. Using code/DB Viewer, add a new entry to the database with the following values:

```text
new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
```

Steps broken down - 

1. Define an sqlite database.

```python
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db = SQLAlchemy(app)
```

2. Create the columns

```python
class movie_list(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String(100), unique=True, nullable=False)
   year = db.Column(db.BigInteger, nullable=False)
   description = db.Column(db.String(500), nullable=False)
   rating = db.Column(db.Float(3))
   ranking = db.Column(db.Integer, nullable=False)
   review = db.Column(db.String(1000), nullable=False)
   img_url = db.Column(db.Text, nullable=False)
```
3. Launch the database

```python
# launch the app
with app.app_context():
    # create the columns
    db.create_all()
```

![03](./images/03.png)

4. Add a new entry

```python
# add new record
with (app.app_context()):
    try:
        # add new data
        new_movie = movie_list(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()
    except:
        print("Duplicate movie title encountered.")
```

5. Make the website take the updated data to render the index page

```python
@app.route("/")
def home():
    return render_template("index.html",
                           title=new_movie.title,
                           date=new_movie.year,
                           rating=new_movie.rating,
                           review=new_movie.review,
                           overview=new_movie.description,
                           link=new_movie.img_url)
```
```html
{% extends 'bootstrap/base.html' %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==" crossorigin="anonymous" />
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}My Top 10 Movies{% endblock %}

{% block content %}
<div class="container">
  <h1 class="heading">My Top 10 Movies</h1>
  <p class="description">These are my all time favourite movies.</p>
   
  <div class="card" >
    <div class="front" style="background-image: url('{{ link }}');">
        <p class="large">{{ rank }}</p>
    </div>
    <div class="back">
      <div>
    <div class="title">{{ title }} <span class="release_date">{{ date }}</span></div>
        <div class="rating">
            <label>{{ rating }}</label>
          <i class="fas fa-star star"></i>
        </div>
          <p class="review">{{ review }}</p>
        <p class="overview">
            {{ overview }}
        </p>

        <a href="#" class="button">Update</a>
        <a href="#" class="button delete-button">Delete</a>

      </div>
    </div>
  </div>
</div>
<div class="container text-center add">
<a href="#" class="button">Add Movie</a>
</div>

{% endblock %}
```

This is the output - 

![04](./images/04.gif)


### 537 Requirement 2 - Be Able to Edit a Movie's Rating and Review

![05](./images/05.gif)

Steps - 

1. When the edit button is clicked, it redirects to another page

```html
<a href="{{ url_for('edit') }}" class="button">Update</a>
```
```python
@app.route("/edit")
def edit():
    return render_template("edit.html")
```

![06](./images/06.gif)

2. The redirected page takes data from index page, during the redirection, and renders using the data

```python
<a href="{{ url_for('edit', movie_name=title) }}" class="button">Update</a>
```

```python
@app.route("/edit/<movie_name>")
def edit(movie_name):
    return render_template("edit.html", movie_name_to_use=movie_name)
```

```html
{% block content %}
<div class="content">
  <h1 class="heading">{{ movie_name_to_use }}</h1>
    <p class="description">Edit Movie Rating</p>
  </div>
{% endblock %}
```

![07](./images/07.gif)

3. The redirected page contains a WTForm, with the fields "Rating" and "Review"

- Create the form in main.py
```python
class MovieForm(FlaskForm):
    rating = FloatField(label='Rating', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField('Submit')
```
- Create the route in main.py
```python
@app.route("/edit/<movie_name>", methods=['GET', 'POST'])
def edit(movie_name):
    form = MovieForm()
    if form.validate_on_submit():
        updated_rating = form.rating.data
        updated_review = form.review.data
    return render_template("edit.html", movie_name_to_use=movie_name, form=form)
```
- Create the form in edit.html
```html
<form method="post" action="{{ url_for('edit', movie_name=movie_name_to_use) }}" novalidate>
{{ wtf.quick_form(form, novalidate=True) }}
</form>
```

4. The data provided in the form updated the new_movie.rating and new_movie.review

```python
@app.route("/edit/<movie_name>", methods=['GET', 'POST'])
def edit(movie_name):
    form = MovieForm()
    if form.validate_on_submit():
        with (app.app_context()):
            movie_to_update = new_movie.query.filter_by(title=movie_name).first()
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()
    return render_template("edit.html", movie_name_to_use=movie_name, form=form)
```

![08](./images/08.png.gif)

5. Upon submitting the form, it redirects back to the home page, with the revised rating and review

So a slight change needs to be made - 

```python
@app.route("/")
def home():
    with (app.app_context()):
        all_movies = db.session.query(movie_list).all()
    return render_template("index.html",
                           # all_movies[0] because the all_movies list currently contains only one element as of now
                           title=all_movies[0].title,
                           date=all_movies[0].year,
                           rating=all_movies[0].rating,
                           review=all_movies[0].review,
                           overview=all_movies[0].description,
                           rank=all_movies[0].ranking,
                           link=all_movies[0].img_url)
```

![09](./images/09.gif)


### 538 Requirement 3 - Be Able to Delete Movies from the Database

- When you click delete on the movie card, it should delete the data from the database
- Also it should reload the index page


```html
<a href="{{ url_for('delete_movie', movie_name=title) }}" class="button delete-button">Delete</a>
```

```python
@app.route("/delete/<movie_name>")
def delete_movie(movie_name):
    with (app.app_context()):
        movie_to_delete = movie_list.query.filter_by(title=movie_name).first()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))
```

### 539 Requirement 4 - Be Able to Add New Movies Via the Add Page

1. Make the add page render when you click on the Add Movie button on the Home page. 
The Add page should show a WTF quick form that only contains 1 field - the title of the movie.
- Create the WTForm in main.py
```python
class AddForm(FlaskForm):
    title = StringField(label='Name Of The Movie', validators=[DataRequired()])
```
- Render the WTForm in add.html
```html
<form method="post" action="{{ url_for('edit', movie_name=movie_name_to_use) }}" novalidate>
{{ wtf.quick_form(form, novalidate=True) }}
</form>
```
- Create a route for the add page
```python
@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    return render_template("add.html", form=form)
```
- Connect the add page with the add button in the home page
```html
<a href="{{ url_for('add') }}" class="button">Add Movie</a>
```
![10](./images/10.gif)

2. When the user types a movie title and clicks "Add Movie", your Flask server should receive the movie title. 
Next, you should use the requests library to make a request and search The Movie Database API for all the movies that match that title.

- Make the form in the add.html receive the form data
- Register in the The Movie Database
- Isolate the data that you need among the results from the API

tmdb.py:
```python
import requests

url = "https://api.themoviedb.org/3/search/movie?query="

class MovieQuery:
    def __init__(self):
        self.url = f"https://api.themoviedb.org/3/search/movie?query="
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MDEyNTgwMDk2ODZmN2I1MGNiNDE5NzQ1MDcxZjNmMCIsInN1YiI6IjY1ZjY1OWYyZTE5NGIwMDE3Y2JlMjhjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dqlbbAIBebEWNSAoDyf7jKb9UGTp49JektSiVEWkBOs",
            }
        self.results = []

    def search(self, movie_name):
        response = requests.get(url+movie_name, headers=self.headers)
        for item in response.json()["results"]:
            self.results.append({"title": item['original_title'], "date": item['release_date']})
        return self.results
```
main.py:
```python
import tmdb

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_query = tmdb.MovieQuery()
        movie = movie_query.search(form.title.data)
        return render_template("select.html", movie_data=movie)
    return render_template("add.html", form=form)
```

3. Using the data you get back from the API, you should render the select.html page and add all the movie title and year of release on to the page. 
This way, the user can choose the movie they want to add. There are usually quite a few movies under similar names.

select.html:
```html
{% block content %}
<div class="container">
    <h1 class="heading">Select Movie</h1>
  <p>
    {% for item in movie_data %}
    <a href="#"> {{ item['title'] }} - {{ item['date'] }}</a>
    <br>
    {% endfor %}
  </p>

</div>
{% endblock %}
```

![11](./images/11.gif)

4. Once the user selects a particular film from the select.html page, the id of the movie needs to be used to hit up another path in the Movie Database API, which will fetch all the data they have on that movie. e.g Poster image URLs.

tmdb.py:
```python
def search_by_id(self, movie_id):
    response = requests.get(self.url_id+str(movie_id), headers=self.headers)
    movie_detail = response.json()
    print(movie_detail)
    self.results_by_id["movie_title"] = movie_detail['original_title']
    self.results_by_id["movie_release_date"] = movie_detail['release_date']
    self.results_by_id["movie_overview"] = movie_detail['overview']
    self.results_by_id["movie_poster"] = movie_detail['poster_path']
    return self.results_by_id
```

select.html:
```html
<p>
{% for elem in movie_data %}
<a href="{{ url_for('select', movie_id=elem['id']) }}"> {{ elem['title'] }} - {{ elem['date'] }}</a>
<br>
{% endfor %}
</p>
```

main.py:
```python
# Select Function
@app.route("/select/<int:movie_id>")
def select(movie_id):
    print(movie_id)
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
    return render_template("index.html")
```

5. Once the entry is added, redirect to the home page and it should display the new movie as a card. Some data will be missing, that's ok.

We need to make a few changes.

First the home route, in main.py:
from this:
```python
# Homepage
@app.route("/")
def home():
    with (app.app_context()):
        all_movies = db.session.query(movie_list).all()
    return render_template("index.html",
                           title=all_movies[0].title,
                           date=all_movies[0].year,
                           rating=all_movies[0].rating,
                           review=all_movies[0].review,
                           overview=all_movies[0].description,
                           rank=all_movies[0].ranking,
                           link=all_movies[0].img_url)

```

to this - 

```python
# Homepage
@app.route("/")
def home():
    with (app.app_context()):
        all_movies = db.session.query(movie_list).all()
    return render_template("index.html", movies_list_with_details=all_movies)
```

So the all_movies list has now been forwarded to the index.html as movies_list_with_details variable.

Accordingly, changes required in the index.html too - 

```html
{% block content %}
<div class="container">
    <h1 class="heading">My Top 10 Movies</h1>
    <p class="description">These are my all time favourite movies.</p>
    {% for card in movies_list_with_details %}

    <div class="card">
        <div class="front" style="background-image: url('{{ card.img_url }}');">
            <p class="large">{{ card.ranking }}</p>
        </div>
        <div class="back">
            <div>
                <div class="title">{{ card.title }} <span class="release_date">{{ card.year }}</span></div>
                <div class="rating">
                    <label>{{ card.rating }}</label>
                    <i class="fas fa-star star"></i>
                </div>
                <p class="review">{{ card.review }}</p>
                <p class="overview">
                    {{ card.description }}
                </p>

                <a href="{{ url_for('edit', movie_name=title) }}" class="button">Update</a>
                <a href="{{ url_for('delete_movie', movie_name=title) }}" class="button delete-button">Delete</a>
            </div>
        </div>
    </div>

    {% endfor %}


</div>
<div class="container text-center add">
    <a href="{{ url_for('add') }}" class="button">Add Movie</a>
</div>
<br>
<br>

{% endblock %}
```

So now, the index file directly takes the list of movies from the sql db and renders the cards accordingly.

![12](./images/12.gif)

6. Instead of redirecting to the home page after finding the correct film, redirect to the edit.html page. 
Because the parts of the movie entry that are missing are the rating and review. 
The form on the edit page will contain these two fields. Update the movie entry in the database with this new data.

Although I think that the previous flow was just fine, once you add a movie, you see it in the homepage.
Then you can always update the rating and review from the homepage.

To do this, we need to reroute the select function to edit page, instead of the home page.
```python
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
```

### 540 Requirement 5 - Be Able to Sort and Rank the Movies By Rating

At the moment the front of the movie card says 0.
Instead, we want it to display the ranking of the movie according to our rating. e.g.
If we gave The Matrix a rating of 9.2 and Spirited Away was rated 9.5 and those are the only 2 movies we've added then it should display Spirited Away with a ranking of 1 and Matrix with a ranking of 2.

That is the idea.

- There is this method in SQLAlchemy called "order_by" - 
![13](./images/13.png)
Use this to sort the movies according to their rating.

```python
# Homepage
@app.route("/")
def home():
    with (app.app_context()):
        all_movies = db.session.query(movie_list).order_by(movie_list.rating)
    return render_template("index.html", movies_list_with_details=all_movies)
```

![14](./images/14.gif)

It gets ordered in reverse, the lower rated movies ranking higher.

In this case, we can use asc() or desc()

![15](./images/15.png)

```python
@app.route("/")
def home():
    with (app.app_context()):
        all_movies = db.session.query(movie_list).order_by(movie_list.rating.desc())
    return render_template("index.html", movies_list_with_details=all_movies)
```

![16](./images/16.gif)

- Once sorted, the IDs of each record will essentially be their rank. Render the ID of a record in front of a card.

Sorted, but the sorting does not change the ID whatsoever,

![17](./images/17.png)

How to do it then?

We could use the list -

```python
all_movies = db.session.query(movie_list).order_by(movie_list.rating.desc())
```

And when rendering in the html, change the card.ranking to the list's index number - 

```html
<p class="large">{{ card.ranking }}</p>
```

to - 

```html
<p class="large">{{ movies_list_with_details.index(card) + 1 }}</p>
```
_+1 because the 1st element in the list has the index 0._

But can we do it without changing the code in the html?

```python
@app.route("/")
def home():
    with (app.app_context()):
        all_movies = db.session.query(movie_list).order_by(movie_list.rating.desc())
        for the_movie in all_movies.all():
            the_movie.ranking = all_movies.all().index(the_movie) + 1
            db.session.commit()
    return render_template("index.html", movies_list_with_details=all_movies.all())
```

Why change `movies_list_with_details=all_movies` to `movies_list_with_details=all_movies.all()`?

```python
print(all_movies)
```
```text
SELECT movie_list.id AS movie_list_id, movie_list.title AS movie_list_title, movie_list.year AS movie_list_year, movie_list.description AS movie_list_description, movie_list.rating AS movie_list_rating, movie_list.ranking AS movie_list_ranking, movie_list.review AS movie_list_review, movie_list.img_url AS movie_list_img_url 
FROM movie_list ORDER BY movie_list.rating DESC
```
```python
print(all_movies.all())
```
```text
[<movie_list 4>, <movie_list 2>, <movie_list 3>, <movie_list 1>]
```

Both will work while iterating, however, `all_movies.index()` does not exist because `all_movies` is not a list.

Thus I changes `all_movies` to `all_movies.all()` everywhere.

Therefore, this is the full website with all the functionalities.

**Final Output**

![Final](./images/Final.gif)

One small change was made.

So now, the feature of adding dummy record before was excluded.
So in the edit page -
```python
movie_to_update = new_movie.query.filter_by(title=movie_name).first()
```
was changed to - 
```python
movie_to_update = movie_list.query.filter_by(title=movie_name).first()
```

That's it.

_**fin**_
