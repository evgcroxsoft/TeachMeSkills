from calendar import weekday
from __init__ import app, db
from models import Register, Habit, Task
from flask_login import current_user, login_required,  logout_user
from flask import flash, redirect, render_template, request, url_for
from datetime import datetime
import datetime

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
    tasks = db.session.query(Task, Habit).join(Habit).all()
    date_now = datetime.date.today()
    for task, habit in tasks:
        print(type(task.start_period), type(date_now))
        if task.start_period >= date_now:
            task = f'{habit.name}'

    return render_template('profile.html', task = task)

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
                        register_id=current_user.id 
                        )
        try:
            db.session.add(habit)
            db.session.commit()
            return redirect(url_for('habits'))
        except:
            flash('Some problem with registration, please try again!')
            return render_template('habits.html')
    habit_check = Habit.query.all()

    return render_template('habits.html', data=habit_check)


@app.route('/profile/habits/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def habits_delete(name,id):
    habit_check = Habit.query.get(id)
    if id and current_user.id == habit_check.register_id or current_user.email == 'admin@admin.com':
        try:
            db.session.delete(habit_check)
            db.session.commit() 
            return redirect(url_for('habits'))
        except:
            flash('Some problem with deleting, please try again!')
            return render_template('habits.html')
        
    return render_template('habits.html')

@app.route('/profile/habits/edit/<name>/<id>', methods=('GET','POST'))
@login_required
def habits_edit(name,id):
    habit_check = Habit.query.get(id)
    if request.method == 'POST' and current_user.id == habit_check.register_id or current_user.email == 'admin@admin.com':
        habit_check.name = request.form['form_name']
        habit_check.description = request.form['form_description']
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
    tasks = db.session.query(Task, Habit).join(Habit).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/profile/habits/tasks/create/<name>/<id>', methods=('GET','POST'))
@login_required
def tasks_create(name,id):
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
        
        habit_id = (Habit.query.get(id)).id

        new_task = Task(
                        wish_period=wish_period,
                        start_period=start_period,
                        weekdays=action_days,
                        habit_id=habit_id,
                        register_id=current_user.id 
                        )
        try:
            db.session.add(new_task)
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with editing, please try again!')
            return render_template('tasks.html')
    return render_template('tasks_create.html', habit=habit, today = datetime.date.today())

@app.route('/profile/habits/tasks/delete/<name>/<id>', methods=('GET','POST','DELETE'))
@login_required
def tasks_delete(name,id):
    task_check = Task.query.get(id)
    if id and current_user.id == task_check.register_id or current_user.email == 'admin@admin.com':
        try:
            db.session.delete(task_check)
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with deleting, please try again!')
            return render_template('tasks.html')
    return render_template('tasks.html')


@app.route('/profile/habits/tasks/edit/<name>/<id>', methods=('GET','POST'))
@login_required
def tasks_edit(name,id):
    task_check = Task.query.get(id)
    tasks = db.session.query(Task, Habit).join(Habit).all()
    
    for task, habit in tasks:
        name = habit.name
        description = habit.description
        wish = task.wish_period
        start = task.start_period

    if request.method == 'POST'and current_user.id == task_check.register_id or current_user.email == 'admin@admin.com':

        weekdays = (request.form['weekday-mon'],
                    request.form['weekday-tue'],
                    request.form['weekday-wed'],
                    request.form['weekday-thu'],
                    request.form['weekday-fri'],
                    request.form['weekday-sat'],
                    request.form['weekday-sun']
        )
        action_days=list(filter(lambda n: n !='off', weekdays))

        task_check.wish_period = request.form['wish_period']
        task_check.start_period = request.form['start_period']
        task_check.weekdays = action_days
    
        try:
            db.session.commit() 
            return redirect(url_for('tasks'))
        except:
            flash('Some problem with editing, please try again!')
            return render_template('tasks.html')
        
    return render_template('tasks_edit.html', name=name, description=description, wish=wish, start=start)