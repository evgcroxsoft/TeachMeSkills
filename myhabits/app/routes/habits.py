from flask import render_template, request
from flask_login import current_user, login_required
from app import app, db
from app.models import User, Habit
from app.db.database import Database
from flask import render_template
from flask import flash, redirect, render_template, url_for

@app.route('/profile/habits', methods=('GET','POST'))
@login_required
def habits():
    if request.method == 'POST':
        habit = Habit(
                    name=request.form['form_name'],
                    description=request.form['form_description'],
                    user_id=current_user.id 
                    )
        table, redirect_url_success, redirect_url_except = habit, 'habits', 'habits'
        Database.add_in_db(table, redirect_url_success, redirect_url_except)

        redirect(url_for(redirect_url_success))
        print(url_for(redirect_url_success))

    all_habits = db.session.query(Habit, User).join(User).order_by(Habit.created.desc()).all()
    return render_template('habits.html', data=all_habits)

@app.route('/profile/habits/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def delete_habit(name,id):
    habit = Habit.query.get(id)
    if id and current_user.id == habit.user_id or current_user.email == 'admin@admin.com':
        
        table, redirect_url_success, redirect_url_except = habit, 'habits', 'habits'
        Database.delete_in_db(table, redirect_url_success, redirect_url_except)

    return render_template('habits.html')

@app.route('/profile/habits/edit/<name>/<id>', methods=('GET','POST'))
@login_required
def update_habit(name,id):
    habit = Habit.query.get(id)
    if request.method == 'POST' and current_user.id == habit.user_id or current_user.email == 'admin@admin.com':
        habit.name = request.form['form_name']
        habit.description = request.form['form_description']
        
        redirect_url_success, redirect_url_except = 'habits', 'habits'
        Database.update_in_db(redirect_url_success, redirect_url_except)
        
    return render_template('habits_edit.html')

