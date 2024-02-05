from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html")


@app.route(rule='/login', methods=['POST'])
def login():
    name_to_use = request.form['fname']
    pass_to_use = request.form['fpass']
    return f"<h1>Username = {name_to_use}, Password = {pass_to_use}</h1>"


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)
