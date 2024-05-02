from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/new-post', methods=['GET', 'POST'])
# need to provide both methods, 'GET' is for redirection from the index page, 'POST' is for data capture from the form
def create_new_post():
    post_form = CreatePostForm()
    if post_form.validate_on_submit():
        # print(post_form.title.data)
        # print(post_form.author.data)
        # print(post_form.body.data)
        today = datetime.datetime.today()
        current_month = today.strftime("%B")
        current_day = today.day
        current_year = today.year
        with (app.app_context()):
            new_blog_entry = BlogPost(
                # id=db.Column(db.Integer, primary_key=True)
                title=post_form.title.data,
                subtitle=post_form.subtitle.data,
                date=f"{current_month} {current_day}, {current_year}",
                body=post_form.body.data,
                author=post_form.author.data,
                img_url=post_form.img_url.data
            )
            db.session.add(new_blog_entry)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template(template_name_or_list="make-post.html", form=post_form)


@app.route("/post/<int:index>")
def show_post(index):
    print(index)
    requested_post = None
    # inside the for loop below there is the argument if blog_post["id"]
    # this means that "posts" should be structured as posts = [{blog post as dict},{same}....{same}]
    posts = []
    for i in BlogPost.query.all():
        posts.append(i.to_dict())
    print(posts)
    for blog_post in posts:
        print(blog_post["id"])
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template(template_name_or_list="post.html", post=requested_post)


@app.route("/edit-post/<post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_be_edited = BlogPost.query.filter_by(id=post_id).first()
    post_form = CreatePostForm(
        title=post_to_be_edited.title,
        subtitle=post_to_be_edited.subtitle,
        img_url=post_to_be_edited.img_url,
        author=post_to_be_edited.author,
        body=post_to_be_edited.body
    )
    if post_form.validate_on_submit():
        print(post_form.body.data)
        with (app.app_context()):
            post_to_be_edited = BlogPost.query.get(post_id)
            post_to_be_edited.title = post_form.title.data
            post_to_be_edited.subtitle = post_form.subtitle.data
            post_to_be_edited.author = post_form.author.data
            post_to_be_edited.img_url = post_form.img_url.data
            post_to_be_edited.body = post_form.body.data
            db.session.commit()
        return redirect(url_for('show_post', index=post_id))
    return render_template(template_name_or_list="make-post.html", form=post_form, edit=True, post_id_num=post_id)


@app.route("/delete/<post_id>")
def delete_post(post_id):
    with (app.app_context()):
        post_to_be_deleted = BlogPost.query.filter_by(id=post_id).first()
        db.session.delete(post_to_be_deleted)
        db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
