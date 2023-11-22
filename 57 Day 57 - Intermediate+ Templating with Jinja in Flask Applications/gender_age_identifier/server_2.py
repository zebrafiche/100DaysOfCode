from flask import Flask, render_template
import genderize
import agify
import requests

app = Flask(__name__)


@app.route("/")
def welcome():
    return '<h1>Welcome to the gender and age identifier.</h1>'


@app.route("/<string:name>")
def gender_age(name):
    sex = genderize.gender(name)
    old = agify.age(name)
    return render_template('index.html', person_name=name, gender=sex.get_gender(), how_old = old.get_age())


@app.route("/blog/<num>")
def get_blog(num):
    url = 'https://api.npoint.io/2694b915f830e8f18aa8'
    response = requests.get(url)
    data = response.json()
    return render_template('blog.html', blog_data=data)


if __name__ == '__main__':
    app.run(debug=True)
