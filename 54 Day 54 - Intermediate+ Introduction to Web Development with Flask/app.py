from flask import Flask
# import random
#
# print(random.__name__)
# print(__name__)
#
# print(Flask.__name__)
# print(__name__)


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

# don't always want to run the app using the terminal, use this -
# if this script is the main module, run the app


if __name__ == "__main__":
    app.run()
