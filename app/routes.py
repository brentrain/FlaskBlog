from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

posts = [
    {
        'author': 'Brent Rainwater',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 6, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'How to Train Cats',
        'content': 'Second post content',
        'date_posted': 'September 5, 2019'
    },
    {
        'author': 'William Williams',
        'title': 'Herding Cats:  A Primer',
        'content': 'Third post content',
        'date_posted': 'September 4, 2019'
    }

]

@app.route('/') # root page of application
@app.route('/home') #home route
def home():
    return render_template ('home.html', posts=posts)

@app.route('/about') #about route
def about():
    return render_template ('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username= form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST']) #login Route
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
            flash('Login Unsuccessful, please try again', 'danger')
    return render_template('login.html', title="Login", form=form)
