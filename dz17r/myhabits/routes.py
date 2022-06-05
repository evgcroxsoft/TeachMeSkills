from __init__ import app, db
from models import Register
from flask_login import LoginManager, login_required,  logout_user
from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return redirect ('home.html')

@app.route('/home')
def home():
    registered = Register.query.all()
    return render_template('home.html', registered = registered)

@app.route('/logout')
def logout():
    pass
    return render_template('logout.html')

@app.route('/user/<nickname>')
def user():
    pass
    return render_template('user.html')

@app.route('/user/<nickname>/about_me')
def about_me():
    pass
    return render_template('about_me.html')

@app.route('/user/<nickname>/my_habits')
def habits_me():
    pass
    return render_template('my_habits.html')