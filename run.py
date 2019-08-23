from flask import Flask, render_template, request, url_for
from forms import RegistrationForm, LoginForm
# adding in functionality to access the operating system
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '37d9b26f4a0cda72818c4c6d4e3a9641'

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
    return render_template("about.html",title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 