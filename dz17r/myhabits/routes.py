from __init__ import app, db
from models import Register, Habit
from flask_login import current_user, login_required,  logout_user
from flask import flash, redirect, render_template, request, url_for

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
    flash('You exit from account')
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    # user_check = Register.query.get(current_user.id)
    # image = base64_encode(user_check.avatar).decode("utf-8")
    return render_template('profile.html')
    # return render_template('profile.html', image=image)

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

@app.route('/profile/habits', methods=('GET','POST'))
@login_required
def habits():
    if request.method == 'POST':
        form_name = request.form['form_name']
        form_description = request.form['form_description']
        habit = Habit(
                        name=form_name,
                        description=form_description, 
                        )
        try:
            db.session.add(habit)
            db.session.commit()
            return redirect(url_for('profile'))
        except:
            flash('Some problem with registration, please try again!')
            return render_template('habits.html')
    habit_check = Habit.query.all()

    return render_template('habits.html', data=habit_check)


@app.route('/profile/habits/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def habits_delete(name,id):
    if id:
        habit_check = Habit.query.get(id)
        try:
            db.session.delete(habit_check)
            db.session.commit() 
            return redirect(url_for('habits'))
        except:
            flash('Some problem with deleting, please try again!')
            return render_template('habits.html')
        
    return render_template('habits.html')
