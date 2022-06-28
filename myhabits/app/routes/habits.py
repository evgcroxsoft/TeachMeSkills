from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import func
from app import app, db
from app.models import User, Habit


@app.route('/profile/habits', methods=('GET','POST'))
@login_required
def habits():
    if request.method == 'POST':
        name = request.form['form_name']
        description = request.form['form_description']
        habit = Habit(
                    name=name,
                    description=description,
                    user_id=current_user.id 
                    )
        try:
            db.session.add(habit)
            db.session.commit()
            return redirect(url_for('habits'))
        except:
            flash('Some problem with registration, please try again!')
            return render_template('habits.html')
    all_habits = db.session.query(Habit, User).join(User).order_by(Habit.created.desc()).all()
    return render_template('habits.html', data=all_habits)

@app.route('/profile/habits/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def delete_habit(name,id):
    habit = Habit.query.get(id)
    if id and current_user.id == habit.user_id or current_user.email == 'admin@admin.com':
        try:
            db.session.delete(habit)
            db.session.commit() 
            return redirect(url_for('habits'))
        except:
            flash('Some problem with deleting, please try again!')
            return render_template('habits.html')
        
    return render_template('habits.html')

@app.route('/profile/habits/edit/<name>/<id>', methods=('GET','POST'))
@login_required
def update_habit(name,id):
    habit = Habit.query.get(id)
    if request.method == 'POST' and current_user.id == habit.user_id or current_user.email == 'admin@admin.com':
        habit.name = request.form['form_name']
        habit.description = request.form['form_description']
        try:
            db.session.commit() 
            return redirect(url_for('habits'))
        except:
            flash('Some problem with editing, please try again!')
            return render_template('habits.html')
        
    return render_template('habits_edit.html')