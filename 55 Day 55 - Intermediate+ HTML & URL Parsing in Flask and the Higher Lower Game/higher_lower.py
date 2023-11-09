from flask import Flask
import random

app = Flask(__name__)

number = random.randint(1, 100)
# print(number)

# user_num = input('Enter a number between 1 and 100 - ')


@app.route("/")
def enter_number():
    return "<h1>Enter a number between 1 and 100</h1>" \
           "<img src='https://media.giphy.com/media/5zoxhCaYbdVHoJkmpf/giphy.gif' style='width:400px;height:400px'>"


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < number:
        return "<h1>Too Low</h1>" \
                "<img src='https://media.giphy.com/media/DVSpPORBAgDwiXCjzf/giphy.gif' style='width:400px;height:300px'>"
    elif guess > number:
        return "<h1>Too High</h1>" \
               "<img src='https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy-downsized-large.gif' style='width:400px;height:300px'>"
    else:
        return "<h1>Perfect</h1>" \
               "<img src='https://media.giphy.com/media/l3q2LH45XElELRzRm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)

