from flask import Flask, render_template
import random
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    today = datetime.now()
    return render_template('index.html', num=random_number, yyyy=today.year)


if __name__ == '__main__':
    app.run(debug=True)
