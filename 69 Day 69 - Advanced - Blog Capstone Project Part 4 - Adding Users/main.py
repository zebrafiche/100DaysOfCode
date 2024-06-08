# from hashlib import md5

from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
# from flask_gravatar import Gravatar
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
# gravatar = Gravatar(app,
#                     size=100,
#                     rating='g',
#                     default='retro',
#                     force_default=False,
#                     force_lower=False,
#                     use_ssl=False,
#                     base_url=None)


# def gravatar_url(email, size=100, rating='g', default='retro', force_default=False):
#     hash_value = md5(email.lower().encode('utf-8')).hexdigest()
#     return f"https://www.gravatar.com/avatar/{hash_value}?s={size}&d={default}&r={rating}&f={force_default}"


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///v5_blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE THE LOGIN MANAGER CLASS
login_manager = LoginManager()
# CONFIGURE THE APP
login_manager.init_app(app)


##CONFIGURE TABLES
# Parent
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="reader")


# Child
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    # author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
    blog_comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    commented_text = db.Column(db.String(500), nullable=False)
    reader_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reader = relationship("User", back_populates="comments")
    parent_post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    parent_post = relationship("BlogPost", back_populates="blog_comments")


# with app.app_context():
#     db.create_all()


# PROVIDING THE USER LOADER CALLBACK
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def admin_only(function):
    @wraps(function)
    # which function? the add_new_post function
    def decorated_function(*args, **kwargs):
        print("decorator works")
        # print(current_user.get_id())
        # print(current_user.is_active)
        if current_user.is_authenticated and current_user.id == 1:
            # if user is authenticated, then show the function (the add_new_post function)
            return function(*args, **kwargs)
        else:
            abort(403)
    return decorated_function


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():

        hashed_password = generate_password_hash(
            password=reg_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )

        with app.app_context():
            new_user = User(
                email=reg_form.email.data,
                name=reg_form.name.data,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template(template_name_or_list="register.html", form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email_or_username_entered = login_form.username_or_email.data
        pass_entered = login_form.password.data
        attempted_user = User.query.filter_by(email=email_or_username_entered).first() or User.query.filter_by(name=email_or_username_entered).first()
        if attempted_user:
            print('User Found')
            print(attempted_user)
            if check_password_hash(attempted_user.password, pass_entered):
                login_user(attempted_user)
                return redirect(url_for('get_all_posts'))
            else:
                print('wrong pass')
                flash('Wrong Password')
                return redirect(url_for('login'))
        else:
            print("username or email not found, kindly register")
            flash('Username or email not found, kindly register')
            return redirect(url_for('register'))
    return render_template(template_name_or_list="login.html", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    print(post_id)
    comment_form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    # print(requested_post.author.name)
    # print(requested_post)
    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            with app.app_context():
                new_comment = Comment(
                    commented_text=comment_form.comment_text.data,
                    reader=current_user,
                    parent_post=BlogPost.query.get(post_id)
                )
                db.session.add(new_comment)
                db.session.commit()
        else:
            flash('Please log in to post a comment')
        return redirect(url_for('show_post', post_id=requested_post.id))
    return render_template("post.html", post=requested_post, form=comment_form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        with (app.app_context()):
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=form.body.data,
                img_url=form.img_url.data,
                author=current_user,
                date=str(date.today().strftime("%B %d, %Y"))
            )
            db.session.add(new_post)
            db.session.commit()
            print('db done')
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)





# rough.rafi@gmail.com
# Rafi
# boingboing

# mushsharat_rahman@gmail.com
# mushthetics
# dingding

