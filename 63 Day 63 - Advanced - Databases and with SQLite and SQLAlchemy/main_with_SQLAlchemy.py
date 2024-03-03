from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


# create an instance of SQLAlchemy
db = SQLAlchemy(app)


# define the class table
class books_read(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String(100), unique=True, nullable=False)
   author = db.Column(db.String(50), nullable=False)
   review = db.Column(db.Float(3))


# launch the app
with app.app_context():
    # create the columns
    db.create_all()


def get_all_books():
    with app.app_context():
        books = db.session.query(books_read).all()
        return books


@app.route('/')
def home():
    all_books = get_all_books()
    return render_template(template_name_or_list='index.html', book_data=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form['fname'],
        author_name = request.form['fauthor'],
        book_rating = request.form['frating']
        # print(book_name[0])
        with app.app_context():
            new_book = books_read(title=book_name[0], author=author_name[0], review=book_rating[0])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/id:<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    with app.app_context():
        book_to_edit = books_read.query.get(book_id)
        name_of_book_to_edit = book_to_edit.title
        rating_of_book_to_edit = book_to_edit.review
    if request.method == 'POST':
        print(request.form["newfrating"])
        with app.app_context():
            book_to_edit = books_read.query.get(book_id)
            book_to_edit.review = request.form["newfrating"]
            print(book_to_edit.review)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',
                           nameofthebook=name_of_book_to_edit,
                           ratingofthebook=rating_of_book_to_edit,
                           idofthebook=book_id)




if __name__ == "__main__":
    app.run(debug=True)

