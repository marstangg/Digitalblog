from flask import Flask, render_template, request, url_for

# adding in functionality to access the operating system
import os

app = Flask(__name__)

posts = [
    {
        'author': 'Marcus Tang',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 24, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 25, 2019'
    }
]


@app.route('/home')
def home():
    return render_template("home.html",posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/greet_the_person', methods=['POST'])
def process_form():
    print(request.form)
    n = request.form.get('person_name')
    age = request.form.get('age')
    return "Hi, {}, welcome to the website!".format(n)


# @app.route('/hello', methods=['GET', 'POST'])
# def foobar():
#     if request.method == 'GET':
#         return render_template("hello.html")
#     elif request.method == 'POST':
#         print(request.form)
#         n = request.form.get('person_name')
#         age = request.form.get('age')
#         return "Hi, {}, welcome to the website".format(n)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 