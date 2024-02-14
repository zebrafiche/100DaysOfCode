from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    url = StringField(label='Location URL', validators=[DataRequired('Provide Location URL'),
                                                        URL(message='Please enter a map location')])
    open_time = TimeField(label='Opening Time', validators=[DataRequired()])
    closing_time = TimeField(label='Closing Time', validators=[DataRequired()])
    # open_time = StringField(label='Opening Time', validators=[DataRequired()])
    # closing_time = StringField(label='Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating',
                                choices=[
                                    ('0', '✘'),
                                    ('1', '☕️'),
                                    ('2', '☕️☕️'),
                                    ('3', '☕️☕️☕️'),
                                    ('4', '☕️☕️☕️☕️'),
                                    ('5', '☕️☕️☕️☕️☕️')
                                ], validators=[DataRequired()])
    wifi_rating = SelectField(label='WiFi Rating',
                                choices=[
                                    ('0', '✘'),
                                    ('1', '💪'),
                                    ('2', '💪💪'),
                                    ('3', '💪💪💪'),
                                    ('4', '💪💪💪💪'),
                                    ('5', '💪💪💪💪💪')
                                ], validators=[DataRequired()])
    power_outlet_rating = SelectField(label='Power Rating',
                                choices=[
                                    ('0', '✘'),
                                    ('1', '🔌'),
                                    ('2', '🔌🔌'),
                                    ('3', '🔌🔌🔌'),
                                    ('4', '🔌🔌🔌🔌'),
                                    ('5', '🔌🔌🔌🔌🔌')
                                ], validators=[DataRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location = form.url.data
        open_time = form.open_time.data
        close_time = form.closing_time.data
        coffee = dict(form.coffee_rating.choices).get(form.coffee_rating.data)
        wifi = dict(form.wifi_rating.choices).get(form.wifi_rating.data)
        power = dict(form.power_outlet_rating.choices).get(form.power_outlet_rating.data)
        with open('cafe-data.csv', mode='a', encoding='UTF-8', newline='') as csv_file:
            csv_edit = csv.writer(csv_file, delimiter=',')
            new_data = [cafe_name, location, open_time, close_time, coffee, wifi, power]
            csv_edit.writerow(new_data)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template(template_name_or_list='add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='UTF-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
