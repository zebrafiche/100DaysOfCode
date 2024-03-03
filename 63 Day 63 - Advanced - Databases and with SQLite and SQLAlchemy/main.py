from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

all_books = []


@app.route('/')
def home():
    return render_template(template_name_or_list='index.html', book_data=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_dict = {
            'book_name': request.form['fname'],
            'author_name': request.form['fauthor'],
            'book_rating': request.form['frating']
        }
        all_books.append(book_dict)
    print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

