from flask import Flask, render_template
import post

app = Flask(__name__)


@app.route('/')
def home():
    blog = post.Post()
    return render_template("index.html", blog_data=blog.get_posts())


@app.route('/post/<int:num>')
def read_post(num):
    blog = post.Post()
    return render_template("post.html", blog_data=blog.get_posts(), number=num)


if __name__ == "__main__":
    app.run(debug=True)
