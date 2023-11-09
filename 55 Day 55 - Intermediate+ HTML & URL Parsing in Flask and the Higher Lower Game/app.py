from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return '<b>'+function()+'</b>'
    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return '<em>'+function()+'</em>'
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return '<u>'+function()+'</u>'
    return wrapper_function


@app.route("/")
@make_bold
@make_italic
@make_underlined
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a para</p>" \
           "<img src='https://miro.medium.com/v2/resize:fit:1024/1*OohqW5DGh9CQS4hLY5FXzA.png'>"


@app.route("/hello")
def say_bye():
    return "Hello"


@app.route("/name/<name>/<int:number>")
def hello(name, number):
    return f"Hello, {name}. You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)

