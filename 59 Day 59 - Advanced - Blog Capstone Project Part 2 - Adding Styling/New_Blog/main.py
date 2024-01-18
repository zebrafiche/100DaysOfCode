from flask import Flask, render_template
import requests

# Get Blog Data
blog_data_url = 'https://api.npoint.io/d23a33f9566fcb4c30e0'

response = requests.get(url=blog_data_url)
print(response.status_code)
data = response.json()
# print(data)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html", data_to_use=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template(template_name_or_list="post.html", data_to_use=data, id_to_use=post_id)


if __name__ == "__main__":
    app.run(debug=True)
