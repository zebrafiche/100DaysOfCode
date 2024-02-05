from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somethingrandom'
Bootstrap(app)


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired("Please enter your email"),
                                                   Email(message='Please enter a valid email.')])
    password = PasswordField(label='Password', validators=[DataRequired("Please enter password"),
                                                           Length(min=8, max=20, message='Requires min 8 characters')])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template('index.html')


@app.route(rule="/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    # if request.method == 'POST':
    #     # return 'Message Captured'
    email_entered = form.email.data
    password_entered = form.password.data
    if form.validate_on_submit():
        if email_entered == 'admin@email.com' and password_entered == '12345678':
            return render_template(template_name_or_list='success.html')
        else:
            return render_template(template_name_or_list='denied.html')
    return render_template(template_name_or_list='login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

