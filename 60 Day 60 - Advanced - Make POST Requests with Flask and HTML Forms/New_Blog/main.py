from flask import Flask, render_template, request
import requests
import mailer

# Get Blog Data
blog_data_url = 'https://api.npoint.io/d23a33f9566fcb4c30e0'

response = requests.get(url=blog_data_url)
print(response.status_code)
data = response.json()
# print(data)

app = Flask(__name__)
new_mail = mailer.Gmailer()


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html", data_to_use=data)


@app.route('/about')
def about():
    return render_template("about.html")


# @app.route('/contact')
# def contact():
#     return render_template("contact.html")


# @app.route(rule='/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name_to_use = request.form['name_entered']
#         email_to_use = request.form['email_entered']
#         phone_to_use = request.form['phone_entered']
#         message_to_use = request.form['message_entered']
#         print(name_to_use, email_to_use, phone_to_use, message_to_use)
#         return f"<h1>Username = {name_to_use}, Email = {email_to_use}, Phone = {phone_to_use}, Message = {message_to_use}</h1>"
#     else:
#         return render_template("contact.html")


@app.route(rule='/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name_to_use = request.form['name_entered']
        email_to_use = request.form['email_entered']
        phone_to_use = request.form['phone_entered']
        message_to_use = request.form['message_entered']
        new_mail.draft_msg(name_to_use, email_to_use, phone_to_use, message_to_use)
        new_mail.send()
        return render_template(template_name_or_list="contact.html", post_status=True)

    else:
        return render_template(template_name_or_list="contact.html")


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template(template_name_or_list="post.html", data_to_use=data, id_to_use=post_id)


if __name__ == "__main__":
    app.run(debug=True)
