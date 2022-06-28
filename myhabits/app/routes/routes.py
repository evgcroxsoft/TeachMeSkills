from flask import flash, redirect, render_template, url_for
from flask_login import  logout_user
from app import app
from app.models import User

@app.route('/')
def index():
    return redirect (url_for('home'))

@app.route('/home')
def home():
    registered = User.query.all()
    return render_template('home.html', registered = registered)

@app.route('/logout')
def logout():
    logout_user()
    flash('You exit from account')
    return redirect(url_for('login'))

