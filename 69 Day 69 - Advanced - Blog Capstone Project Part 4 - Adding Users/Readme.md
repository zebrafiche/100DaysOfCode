### 577 Day 69 Goals - Adding Users to Our Blog Project

Wouldn't it be great if we could have some users on our blog? 
What if we could let anyone sign up and comment on our blog posts? In order for that to work, 
we would need to add authentication to our blog. This will be the final step in our Blog Capstone Project. 
Once we're done, it will be a fully-fledged blog website that you can publish and launch.

This is what you'll make by the end:

![01](./images/01.gif)


### 578 Download the Starting Project


### 579 Requirement 1 - Register New Users

1. Use what you've learnt yesterday to allow users to go to the /register route to sign up to your blog website. 
You should create a WTForm in forms.py called RegisterForm and use Flask-Bootstrap to render a wtf quick_form.

The data the user entered should be used to create a new entry in your blog.db in a User table.

Steps

1. When the user clicks "Register" from the homepage, s/he should be able to see a form in the register page.

- Create the form

forms.py -
```python
class RegisterForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    name = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Register")
```

main.py - 
```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm()
    return render_template(template_name_or_list="register.html", form=reg_form)
```

- Render the form in the register page - 

register.html - 
```html
{{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
```

2. When the user fills out the form, the data gets stored in another table named "users" in the database.

- Create a new table named "users" in the existing database.

main.py - 
```python
# this is the previous table, some data have already been added to it
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    
# this is the new table we are creating
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

# the below code to be run just once to create the tables 
with app.app_context():
    db.create_all()
```

[db.create_all() doesn’t modify any existing entry. 
If there is a model that is not present in the current db schema it’s going to add it.](https://www.reddit.com/r/flask/comments/pgvne7/am_confused_about_the_best_way_to_add_a_new_table/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

- Now that the new table is created, make it so that when the user registers from the register.html page, his data gets captured.

register.html -
```html
<div class="col-lg-8 col-md-10 mx-auto">
    <form method="post" action="{{ url_for('register') }}" novalidate>
        {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
    </form>
</div>
```

- Make it so that the data captured gets stored in the "users" table, with the password hashed.

main.py - 
```python
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
```


### 580 Requirement 2 - Login Registered Users

1. Users who have been successfully registered (added to the user table in the database) should be able to go to 
the /login route to use their credentials to log in.

- Initiate Flask-login
```python
# CREATE THE LOGIN MANAGER CLASS
login_manager = LoginManager()
# CONFIGURE THE APP
login_manager.init_app(app)
```

After the User table has been declared, the code below should be added
```python
# PROVIDING THE USER LOADER CALLBACK
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
```

Now we come to the login route.
But where is the form? We should have a form in the login page too.
- Create the login form in the forms.py
```python
class LoginForm(FlaskForm):
    username_or_email = StringField(label="Username or Email", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Login")
```

- Now in the login route, create the login form object - 
```python
@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template("login.html")
```

- The login form object should be sent to the login.html so that the form gets rendered
```python
@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)
```
login.html - 
```html
<div class="col-lg-8 col-md-10 mx-auto content">
    <form method="post" action="{{ url_for('login') }}" novalidate>
        {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
    </form>
</div>
```

- If the login form is submitted and the inputs validated, then it should redirect to the homepage.
```python
@app.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=login_form)
```

- Capture the "email or username" input in the form
```python
@app.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email_or_username_entered = login_form.username_or_email.data
        return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=login_form)
```

- Check the username or the email entered by the user against both the "name" column and the "email" column
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email_or_username_entered = login_form.username_or_email.data
        attempted_user = User.query.filter_by(email=email_or_username_entered).first() or User.query.filter_by(name=email_or_username_entered).first()
        if attempted_user:
            print('User Found')
        return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=login_form)
```

```commandline
User Found
```

- If the user passes the "username or email" check, then check the password
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email_or_username_entered = login_form.username_or_email.data
        pass_entered = login_form.password
        attempted_user = User.query.filter_by(email=email_or_username_entered).first() or User.query.filter_by(name=email_or_username_entered).first()
        if attempted_user:
            # print('User Found')
            if check_password_hash(attempted_user.password, pass_entered):
                login_user(attempted_user)
                return redirect(url_for('get_all_posts'))
            else:
                print('wrong pass')
        else:
            print("username or email not found, kindly register")
    return render_template(template_name_or_list="login.html", form=login_form)
```

![02](./images/02.gif)


- WHen the username/email is not found in the database, send the user to the register page
```python
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
        else:
            print("username or email not found, kindly register")
            return redirect(url_for('register'))
    return render_template(template_name_or_list="login.html", form=login_form)
```

- Flash messages when (i) Email not found, (ii) Wrong pass 
main.py
```python
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
```
login.html
```html
<div class="container">
    <div class="row">
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul class=flashes>
            {% for message in messages %}
            <p style="font-style: italic; color:red;">{{ message }}</p>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        <div class="col-lg-8 col-md-10 mx-auto content">
            <form method="post" action="{{ url_for('login') }}" novalidate>
                {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
            </form>
        </div>
    </div>
</div>
```

register.html
```html
<div class="container">
    <div class="row">
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul class=flashes>
            {% for message in messages %}
            <p style="font-style: italic; color:red;">{{ message }}</p>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        <div class="col-lg-8 col-md-10 mx-auto">
            <form method="post" action="{{ url_for('register') }}" novalidate>
                {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
            </form>
        </div>
    </div>
</div>
```

- Adjust the navbar so the 'Login' and 'Register' buttons do not, and a 'Logout' button do, show while logged in

header.html
```html
{% if not current_user.is_authenticated %}
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('login') }}">Login</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('register') }}">Register</a>
</li>
{% else %}
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('logout') }}">Log Out</a>
</li>
{% endif %}
```

- Code up the /logout route so that when the user clicks on the LOG OUT button, it logs them out and takes them back to the home page.

```python
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))
```

![03](./images/03.gif)


### 581 Requirement 3 - Protect Routes

In our blog, the first registered user will be the admin. 
They will be able to create new blog posts, edit posts and delete posts.

1. The first user's id is 1. 
We can use this in index.html and post.html to make sure that only the admin user can see the "Create New Post" and "Edit Post" and Delete buttons.

index.html - 
```html
<p class="post-meta">Posted by
    <a href="#">{{post.author}}</a>
    on {{post.date}}
    {% if current_user.id == 1 %}
    <a href="{{url_for('delete_post', post_id=post.id) }}">✘</a>
    {% endif %}

</p>



{% if current_user.id == 1 %}
<div class="clearfix">
    <a class="btn btn-primary float-right" href="{{url_for('add_new_post')}}">Create New Post</a>
</div>
{% endif %}
```

post.html
```html
{% if current_user.id == 1 %}
<div class="clearfix">
<a class="btn btn-primary float-right" href="{{url_for('edit_post', post_id=post.id)}}">Edit Post</a>
</div>
{% endif %}
```

2. Just because a user can't see the buttons, 
they can still manually access the /edit-post or /new-post or /delete routes. 
Protect these routes by creating a Python decorator called @admin_only

If the current_user's id is 1 then they can access those routes, 
otherwise, they should get a 403 error (not authorised).

- the logic
```python
if current_user.is_authenticated and current_user.id == 1:
    # if user is authenticated, then show the function (the add_new_post function)
    return function(*args, **kwargs)
```
- the abort function
```python
else:
    abort(403)
```
- the decorator
```python
def admin_only(function):
    @wraps(function)
    # which function? the add_new_post function
    def decorated_function(*args, **kwargs):
        print("decorator works")
        # print(current_user.get_id())
        # print(current_user.is_active)
        if current_user.is_authenticated and current_user.id == 1:
            # if user is authenticated with id = 1, then show the function (the add_new_post function)
            return function(*args, **kwargs)
        else:
            # otherwise abort
            abort(403)
    return decorated_function
```
- the application
```python
@app.route("/new-post")
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)
```

![04](./images/04.gif)

Protect the edit and delete routes too, to be only visible to the admin.

Just add @admin_only before the code.

```python
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
```

### 582 Creating Relational Databases

Currently, at the database level, the two tables are not connected.

We would essentially want to connect each blog post to the user who has written it.

How can we do it on a database level?

1. Modify the User (Parent) and BlogPost (Child) class code to create a bidirectional One-to-Many relationship between the two tables. 
You should be able to easily locate the BlogPosts a User has written and also the User of any BlogPost object.

- the doc

from the docs

**One To Many**
A one to many relationship places a foreign key on the child table referencing the parent. 
`relationship()` is then specified on the parent, 
as referencing a collection of items represented by the child:

```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
```

To establish a bidirectional relationship in one-to-many, where the “reverse” side is a many to one, 
specify an additional `relationship()` and connect the two using the `relationship.back_populates` parameter:

```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")
```

Child will get a parent attribute with many-to-one semantics.

Alternatively, the `relationship.backref` option may be used on a single `relationship()` instead of using `relationship.back_populates`:

```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")
```

- the code change in the class

So the user will be my parent and the blogposts will be my children.

```python
##CONFIGURE TABLES
# Parent
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    children = relationship("BlogPost", back_populates="author")


# Child
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # the old author column was a simple string, modify it so it auto populates from whoever is writing the post
    author = relationship("User", back_populates="children")
    # author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()
```

**Re-creating the Database after changes to the Schema**
If you re-run your blog at this point you'll get an error:

`OperationalError: (sqlite3.OperationalError) no such column: blog_posts.author_id`

The reason is that our new code in the main.py modifies our database model by adding a new column into our 
database that was not present in the original blog.db  from the starter code:

```python
parent_id = db.Column(db.Integer, db.ForeignKey('users.id'))
```

We don't have any valuable data at this point that we'd like to preserve, so the easiest way to simply delete the existing blog.db entirely and to use the line db.create_all() to re-create all the tables from scratch. 
Remember, this means you also have to register your user again and create a post since we've just wiped our database.

Now if you refresh your Blog website, you'll see the author name disappear from the index.html and page.html pages.

2. Modify the index.html and post.html pages so that the author name is still displayed in the right places.

index.html - 
```html
<p class="post-meta">Posted by
    <a href="#">{{current_user.name}}</a>
    on {{post.date}}
    {% if current_user.id == 1 %}
    <a href="{{url_for('delete_post', post_id=post.id) }}">✘</a>
    {% endif %}

</p>
```

post.html - 
```html
<span class="meta">Posted by
  <a href="#">{{current_user.name}}</a>
  on {{post.date}}
</span>
```

### 583 Requirement 4 - Allow Any User to Add Comments to BlogPosts

1. Create a CommentForm in the form.py file it will only contain a single CKEditorField for users to write their comments.

forms.py - 
```python
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
```

main.py - 
```python
@app.route("/post/<int:post_id>")
def show_post(post_id):
    comment_form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post, form=comment_form)
```

post.html - 
```html
{% import 'bootstrap/wtf.html' as wtf %}

<!--inserting this at the bottom of the page-->
<div class="container">
    <div class="row">
        <div class="col-lg-10 col-md-10 mx-auto">
            <form method="post" action="{{ url_for('get_all_posts') }}" novalidate>
                {{ ckeditor.load() }}
                {{ ckeditor.config(name='comment_body') }}
                {{ form.csrf_token }}
                {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
            </form>
        </div>
    </div>
</div>
```

The next step is to allow users to leave a comment and save the comment. 
Now that we've seen how relationships can be established between tables in our database. 
Let's step up our relationships to create a new Table where any user can write comments to our blog posts.

2. Create a Table called `Comment` where the tablename is "comments". 
It should contain an id and a text property which will be the primary key and the text entered into the CKEditor.

```python
##CONFIGURE TABLES
# Parent
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    children = relationship("BlogPost", back_populates="author")


# Child
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates="children")
    # author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# This is where the new table will go
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    commented_text = db.Column(db.String(500), nullable=False)

# Run this the first time only, after you have made any changes to the database    
# with app.app_context():
#     db.create_all()
```

3. Establish a One to Many relationship Between the User Table (Parent) and the Comment table (Child). 
Where One User is linked to Many Comment objects.

![05](./images/05.png)

At this point, it is better to change the existing tables a bit.

These - 
```python
children = relationship("BlogPost", back_populates="author")
```
```python
author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
author = relationship("User", back_populates="children")
```
Changed to - 
```python
posts = relationship("BlogPost", back_populates="author")
```
```python
author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
author = relationship("User", back_populates="comments")
```

This way now that we have to create another set of children, i.e. comments, there won't be any confusion.

Now let's create the relationship - 

```python
# The parent, understandably, is the user.
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    # Here is where the new relationship is established
    comments = relationship("Comment", back_populates="reader")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    # Every comment will have a reader id, which is essentially just the uesr id
    reader_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Here every comment is tagged with the reader who made the comment
    reader = relationship("User", back_populates="comments")
    commented_text = db.Column(db.String(500), nullable=False)
```

Apart from each user having many comments, each blogpost can have many comments as well.

4. Establish a One to Many relationship between each BlogPost object (Parent) and Comment object (Child). 
Where each BlogPost can have many associated Comment objects.

```python
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
    # author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    blog_comments = relationship("Comment", back_populates="the_post")

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    reader_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reader = relationship("User", back_populates="comments")
    the_post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    the_post = relationship("BlogPost", back_populates="blog_comments")
    commented_text = db.Column(db.String(500), nullable=False)
```

5. The comments form, once filled, should populate the db. Code in the route.

Issues -
- post_id and reader_id does not get posted in the comments database
  - when post and reader parameter is added, throws `sqlalchemy.exc.InvalidRequestError: Object '<BlogPost at 0x1dcb7c56540>' is already attached to session '3' (this is '4')`
    ```python
    @app.route("/post/<int:post_id>", methods=['GET', 'POST'])
    def show_post(post_id):
        print(post_id)
        comment_form = CommentForm()
        requested_post = BlogPost.query.get(post_id)
        print(requested_post)
        if comment_form.validate_on_submit():
            with app.app_context():
                new_comment = Comment(
                    commented_text=comment_form.comment_text.data,
                    reader=current_user,
                    parent_post=requested.post
                )
                db.session.add(new_comment)
                db.session.commit()
                return redirect(url_for('show_post', post_id=requested_post.id))
        return render_template("post.html", post=requested_post, form=comment_form)
    ```
  - is the problem in the table design?
    - no, checked by changing the parameters. code throws error then. not now
  - **fixed this by changing `requested.post` to `BlogPost.query.get(post_id)`**
    ```python
    @app.route("/post/<int:post_id>", methods=['GET', 'POST'])
    def show_post(post_id):
        print(post_id)
        comment_form = CommentForm()
        requested_post = BlogPost.query.get(post_id)
        print(requested_post)
        if comment_form.validate_on_submit():
            with app.app_context():
                new_comment = Comment(
                    commented_text=comment_form.comment_text.data,
                    reader=current_user,
                    parent_post=BlogPost.query.get(post_id)
                )
                db.session.add(new_comment)
                db.session.commit()
            return redirect(url_for('show_post', post_id=requested_post.id))
        return render_template("post.html", post=requested_post, form=comment_form)
    ```
  - post author shows name of the current user, instead of showing author's name 
    - changed `current.user.name` to `post.author.name`
    _index.html - _
    ```html
    <p class="post-meta">Posted by
        <a href="#">{{post.author.name}}</a>
        on {{post.date}}
        {% if current_user.id == 1 %}
        <a href="{{url_for('delete_post', post_id=post.id) }}">✘</a>
        {% endif %}
  
    </p>
    ```
    _post.html -_ 
    ```html
    <div class="col-lg-8 col-md-10 mx-auto">
        <div class="post-heading">
            <h1>{{post.title}}</h1>
            <h2 class="subheading">{{post.subtitle}}</h2>
            <span class="meta">
                Posted by
      <a href="#">{{post.author.name}}</a>
      on {{post.date}}
             </span>
        </div>
    </div>
    ```

- what if I want to change the db file name from blog.db to v3_blog.db?
```python
##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///v3_blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```

- Make sure that only authenticated (logged-in) users can save their comment. 
Otherwise, they should see a flash message telling them to log in and redirect them to the /login route.

- the post route should have an argument to this effect
  - can we do this using current_user?
    - Nope, throws `AttributeError: 'AnonymousUserMixin' object has no attribute '_sa_instance_state'` error
    - this is because the current_user always has an object, when logged in it has a user object, when not, it has a 'AnonymousUserMixin' object
  - we can do this with `current_user.is_authenticated`
    - main.py - 
    ```python
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
    ```
- also update the post.html
```html
<div class="container">
    <div class="row">
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul class=flashes>
            {% for message in messages %}
            <p style="font-style: italic; color:red;">{{ message }}</p>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        <div class="col-lg-10 col-md-10 mx-auto">
            <form method="post" action="{{ url_for('show_post', post_id=post.id) }}" novalidate>
                {{ ckeditor.load() }}
                {{ ckeditor.config(name='comment_body') }}
                {{ form.csrf_token }}
                {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "primary"}) }}
            </form>
        </div>
    </div>
</div>
```

![06](./images/06.gif)


6. The post page, should take all comments from the db and display them

- We could use `all_comments = Comments.query.all()` but that would list all comments, not just the comments made on the post specifically.
- We want only the comments made in the post. Each post has a comments object as children.
```html
<!--           Comments Area -->
{% for one_comment in post.blog_comments %}
<div class="col-lg-8 col-md-10 mx-auto comment">
    <ul class="commentList">
        <li>
            <div class="commenterImage">
                <img src="https://pbs.twimg.com/profile_images/744849215675838464/IH0FNIXk.jpg"/>
            </div>
            <div class="commentText">
                <p>{{ one_comment.commented_text }}</p>
                <span class="date sub-text">{{ one_comment.reader.name }}</span>
            </div>
        </li>
    </ul>
</div>
```

- Issue - 
  - The comments get posted like this - 
    
    [07](./images/07.png)
    - Use the |safe filter in jinza to avoid this
      - ```html
              <!--           Comments Area -->
        {% for one_comment in post.blog_comments %}
        <div class="col-lg-8 col-md-10 mx-auto comment">
            <ul class="commentList">
                <li>
                    <div class="commenterImage">
                        <img src="https://pbs.twimg.com/profile_images/744849215675838464/IH0FNIXk.jpg"/>
                    </div>
                    <div class="commentText">
                        <p>{{ one_comment.commented_text|safe }}</p>
                        <span class="date sub-text">{{ one_comment.reader.name }}</span>
                    </div>
                </li>
            </ul>
        </div>
        ```

7. Use Gravatar to assign images to each commenter.

- Issue - The updated version of Flask such as this does not support Gravatar anymore.
  - There are various **_unofficial_** workarounds.
    - https://gist.github.com/angelabauer/70d5fa9b62654cd40f4df92f3a196a02?permalink_comment_id=4873282#gistcomment-4873282


#### fin
