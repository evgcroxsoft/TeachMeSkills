from __init__ import app, db
from models import Register
from flask_login import LoginManager, current_user, login_required,  logout_user
from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return redirect (url_for('home'))

@app.route('/home')
def home():
    registered = Register.query.all()
    return render_template('home.html', registered = registered)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name = current_user.email)

@app.route('/profile/about_me', methods=('GET','POST'))
@login_required
def about_me():
    user_check = Register.query.get(current_user.id)
    if request.method == 'POST':
        user_check.nickname = request.form['nickname']
        user_check.name = request.form['name']
        user_check.surname = request.form['surname']
        user_check.birthday = request.form['birthday']
        user_check.telegram = request.form['telegram']
        user_check.colour = request.form['colour']
        user_check.avatar_name = request.files['avatar'].filename
        user_check.avatar = request.files['avatar'].read()
        user_check.gender = request.form['gender']
        user_check.my_info = request.form['my_info']
        
        try:
            db.session.commit()
            return redirect(url_for('profile'))
        except:
            flash('Some problem with saving, try again!')
            return redirect(url_for('about_me'))
        
    return render_template('about_me.html')

@app.route('/user/<nickname>/my_habits')
def habits_me():
    pass
    return render_template('my_habits.html')