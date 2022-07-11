from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import func
from app import app, db
from app.models import Habit, Task
from app.services.utils import date_now


@app.route('/profile/habits/tasks', methods=('GET','POST'))
@login_required
def tasks():
    tasks = db.session.query(Task, Habit).join(Habit).order_by(Task.created.desc()).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/profile/habits/tasks/create/<name>/<id>', methods=('GET','POST'))
@login_required
def tasks_create(name ,id):
    habit = Habit.query.get(id)
    if request.method == 'POST':
        wish_period = request.form['wish_period']
        start_period = request.form['start_period']
        weekdays = (request.form['weekday-mon'],
                    request.form['weekday-tue'],
                    request.form['weekday-wed'],
                    request.form['weekday-thu'],
                    request.form['weekday-fri'],
                    request.form['weekday-sat'],
                    request.form['weekday-sun']
        )
        action_days=list(filter(lambda n: n !='off', weekdays))
        
        habit_id = habit.id

        new_task = Task(
                        wish_period=wish_period,
                        start_period=start_period,
                        weekdays=action_days,
                        habit_id=habit_id,
                        user_id=current_user.id 
                        )
        try:
            db.session.add(new_task)
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with editing, please try again!')
            return render_template('tasks.html')
    return render_template('tasks_create.html', habit=habit, today = date_now())

@app.route('/profile/habits/tasks/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def tasks_delete(name,id):
    task = Task.query.get(id)
    if id and current_user.id == task.user_id or current_user.email == 'admin@admin.com':
        try:
            db.session.delete(task)
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with deleting, you can not delete if task was checked!')
            db.session.rollback()
            return render_template('tasks.html')
    return render_template('tasks.html')


@app.route('/profile/habits/tasks/edit/<name>/<id>', methods=('GET','POST'))
@login_required
def tasks_edit(name,id):
    task = Task.query.get(id)
    tasks = db.session.query(Task, Habit).join(Habit).all()
    
    for task, habit in tasks:
        name = habit.name
        description = habit.description
        wish = task.wish_period
        start = task.start_period

    if request.method == 'POST'and current_user.id == task.user_id or current_user.email == 'admin@admin.com':
        weekdays = (request.form['weekday-mon'],
                    request.form['weekday-tue'],
                    request.form['weekday-wed'],
                    request.form['weekday-thu'],
                    request.form['weekday-fri'],
                    request.form['weekday-sat'],
                    request.form['weekday-sun']
        )
        action_days=list(filter(lambda n: n !='off', weekdays))

        task.wish_period = request.form['wish_period']
        task.start_period = request.form['start_period']
        task.weekdays = action_days
    
        try:
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with editing, please try again!')
            return render_template('tasks.html')
        
    return render_template('tasks_edit.html', name=name, description=description, wish=wish, start=start, today = date_now())