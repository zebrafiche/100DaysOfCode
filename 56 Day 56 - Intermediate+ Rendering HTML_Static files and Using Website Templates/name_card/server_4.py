from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('index.html')


@app.route('/1')
def link1():
    # return render_template('index.html')
    return redirect("https://www.linkedin.com/in/a-a-rafi", code=302)


@app.route('/2')
def link2():
    # return render_template('index.html')
    return redirect("https://github.com/a-a-rafi", code=302)


@app.route('/3')
def link3():
    # return render_template('index.html')
    return redirect("https://www.facebook.com/rough.rafi/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

