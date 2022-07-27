from flask import render_template, request
from flask_login import current_user, login_required
from application import app, db
from application.models import User, Habit
from application.db_myhabits.database import Crud
from flask import render_template
from flask import redirect, render_template, url_for

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
        Crud.add_in_db(table, redirect_url_success, redirect_url_except)

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
        Crud.delete_in_db(table, redirect_url_success, redirect_url_except)

    return render_template('habits.html')

@app.route('/profile/habits/edit/<name>/<id>', methods=('GET','POST'))
@login_required
def update_habit(name,id):
    habit = Habit.query.get(id)
    if request.method == 'POST' and current_user.id == habit.user_id or current_user.email == 'admin@admin.com':
        habit.name = request.form['form_name']
        habit.description = request.form['form_description']
        
        redirect_url_success, redirect_url_except = 'habits', 'habits'
        Crud.update_in_db(redirect_url_success, redirect_url_except)
        
    return render_template('habits_edit.html')

