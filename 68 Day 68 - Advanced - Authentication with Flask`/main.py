from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


## CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# with app.app_context():
#     db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        user_password = request.form['password']
        hashed_password = generate_password_hash(
            password=user_password,
            method='pbkdf2:sha256',
            salt_length=8
        )
        # print(hashed_password)
        # print(user_password)
        if User.query.filter_by(email=user_email).first():
            flash(message="Email already exists in the DB", category="info")
            return redirect(url_for('login'))
        else:
            with app.app_context():
                new_user = User(
                    name=user_name,
                    email=user_email,
                    password=hashed_password
                )
                db.session.add(new_user)
                db.session.commit()
            attempted_user = User.query.filter_by(email=user_email).first()
            login_user(attempted_user)
            return render_template(
                template_name_or_list="secrets.html"
            )
    return render_template("register.html")


@app.route(rule='/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_entered = request.form['email']
        # print(email_entered
        pass_entered = request.form['password']
        # print(pass_entered)
        attempted_user = User.query.filter_by(email=email_entered).first()
        if not attempted_user:
            flash(message="That email does not exist in the db", category="info")
            return redirect(url_for('login'))
        # print('here')
        # print(attempted_user)
        # print(attempted_user.password)
        else:
            if check_password_hash(attempted_user.password, pass_entered):
                # print('pass checked')
                login_user(attempted_user)
                return render_template(
                    template_name_or_list="secrets.html"
                )
            else:
                flash('Wrong Password')
                return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
    pass


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="./static/files",
        path="cheat_sheet.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)










# Test IDs and passes:
#
# mushsharat_rahman
# mushthtetics
#
# keyan_rahman
# abdullah
#
# pritom_hasan
# pritomhasan
#
# shafi_abdullah
# rabid
#
# ayushi_misra
# ayushimisra


