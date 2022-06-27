from datetime import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required,  logout_user
from sqlalchemy import func
from __init__ import app, db
from models import User, Habit, Task

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

@app.route('/profile/about_me', methods=('GET','POST'))
@login_required
def about_me():
    user = User.query.get(current_user.id)
    if request.method == 'POST':
        user.nickname = request.form['nickname']
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.birthday = request.form['birthday']
        user.telegram = request.form['telegram']
        user.colour = request.form['colour']
        user.avatar_name = request.files['avatar'].filename
        user.avatar = request.files['avatar'].read()
        user.gender = request.form['gender']
        user.my_info = request.form['my_info']
        
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
    habit = db.session.query(Habit, User).join(User).order_by(Habit.created.desc()).all()
    return render_template('habits.html', data=habit)

@app.route('/profile/habits/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def delete_habit(name,id):
    habit = Habit.query.get(id)
    if id and current_user.id == habit.register_id or current_user.email == 'admin@admin.com':
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
    if request.method == 'POST' and current_user.id == habit.register_id or current_user.email == 'admin@admin.com':
        habit.name = request.form['form_name']
        habit.description = request.form['form_description']
        try:
            db.session.commit() 
            return redirect(url_for('habits'))
        except:
            flash('Some problem with editing, please try again!')
            return render_template('habits.html')
        
    return render_template('habits_edit.html')

@app.route('/profile/habits/tasks', methods=('GET','POST'))
@login_required
def tasks():
    tasks = db.session.query(Task, Habit).join(Habit).order_by(Task.created.desc()).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/profile/habits/tasks/create/<name>/<id>', methods=('GET','POST'))
@login_required
def tasks_create(name ,id):
    habit = Habit.query.get(id)
    date_now = datetime.date.today()
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
        
        habit = (Habit.query.get(id)).id

        new_task = Task(
                        wish_period=wish_period,
                        start_period=start_period,
                        weekdays=action_days,
                        habit_id=habit,
                        user_id=current_user.id 
                        )
        try:
            db.session.add(new_task)
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with editing, please try again!')
            return render_template('tasks.html')
    return render_template('tasks_create.html', habit=habit, today = date_now)

@app.route('/profile/habits/tasks/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def tasks_delete(name,id):
    task = Task.query.get(id)
    if id and current_user.id == task.register_id or current_user.email == 'admin@admin.com':
        try:
            db.session.delete(task)
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with deleting, please try again!')
            return render_template('tasks.html')
    return render_template('tasks.html')


@app.route('/profile/habits/tasks/edit/<name>/<id>', methods=('GET','POST'))
@login_required
def tasks_edit(name,id):
    date_now = datetime.date.today()
    task = Task.query.get(id)
    tasks = db.session.query(Task, Habit).join(Habit).all()
    
    for task, habit in tasks:
        name = habit.name
        description = habit.description
        wish = task.wish_period
        start = task.start_period

    if request.method == 'POST'and current_user.id == task.register_id or current_user.email == 'admin@admin.com':
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
        
    return render_template('tasks_edit.html', name=name, description=description, wish=wish, start=start, today = date_now)