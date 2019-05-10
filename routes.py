from falsktest1 import app
from flask import flash, redirect, render_template, url_for
from falsktest1.forms import LoginForm, RegistrationForm
from falsktest1.models import User, Post
posts = [    {'author':'Anand', 'title':'blog title1', 'content':'first postt','date_posted':'8th may 2019'},
    {   'author':'someoneelse', 'title':'blog title2', 'content':'second postt','date_posted':'9th may 2019'
    }
]
@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit(): 
        flash('Account Created for {}!'.format(form.username.data),'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        flash('Signed In As {}!'.format(form.email.data),'success')
        return redirect(url_for('home'))
    return render_template('login.html',title='Login', form=form)
