from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# create an instance of SQLAlchemy
db = SQLAlchemy(app)


# define the class table
class books_read(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   # primary_key=True means the value will be unique
   title = db.Column(db.String(100), unique=True, nullable=False)
   # db.String(20) means the max length of the string will be 20 characters.
   # The primary key will not accept NULL values whereas the Unique key can accept NULL values.
   # A table can have only one primary key whereas there can be multiple unique keys on a table.
   author = db.Column(db.String(50), nullable=False)
   review = db.Column(db.Float(3))



# # launch the app
# with app.app_context():
#     # create the columns
#     db.create_all()

# with app.app_context():
#     # set up an instance of the books_read class
#     harry_potter = books_read(title='Harry Potter 5', author='J. K. Rowling', review=4.5)
#     # add the book
#     db.session.add(harry_potter)
#     # commit the changes into the database, you can add a number of books before committing
#     db.session.commit()

with app.app_context():
    all_books = db.session.query(books_read).all()
    print(all_books)
    for book in all_books:
        print(book.title, book.author, book.review, book.id)


with app.app_context():
    my_book = books_read.query.get(3)
    print(my_book.title)

