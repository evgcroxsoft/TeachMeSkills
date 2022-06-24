from __init__ import app, db
from flask_login import current_user, login_required
from models import Task, Habit, Statistic
from datetime import datetime, date
import datetime
from flask import flash, redirect, render_template, request, url_for

@app.route('/profile', methods=('GET','POST'))
@login_required
def profile():
    tasks = db.session.query(Task, Habit).filter_by(register_id = current_user.id).join(Habit).all()
    date_now = datetime.date.today()
    weekday_now = datetime.datetime.today().strftime('%A')
    # statistic = Statistic.query.filter_by(register_id = current_user.id).all()
    # total_counter = Statistic.query.with_entities(func.sum(Statistic.counter).label('total')).first().total
    # query = db.select([db.func.round(db.func.sum(statistic.counter))])
    ids = []
    for task, habit in tasks:
        # if current_user.id == task.register_id:
            if task.start_period <= date_now:
                # if total_counter == None or total_counter >= 0:
                #     total_counter = 0
                #     if task.wish_period - total_counter !=0:
                            for day in task.weekdays:
                                if day == weekday_now:
                                    ids.append(task.id)
    ids1 = []
    for i in ids:
        if Statistic.query.filter_by(task_id = i).all():
            print (Statistic.query.filter_by(task_id = i).all())
        ids1.append(i)
    task_statistic = Statistic.query.filter(Statistic.task_id.in_(ids)).all()
    print('STEP 1',task_statistic)
   
    if task_statistic != []:
        print('Spep 2')
        for no_done_task in task_statistic:
            print(no_done_task.counter)
            # if no_done_task.task_id !=
                # if no_done_task.counter < 1:
                #     print(no_done_task.counter, no_done_task.task_id)
                # if no_done_task.task_id != True:
                #     print('Spep 3')
                    # ids1.append(no_done_task.task_id)
    print(ids)
    print(ids1)
    # print(task_statistic)
    today_tasks = db.session.query(Task, Habit).filter(Task.id.in_(ids)).join(Habit).all()

    if request.method == 'POST':
        # print(request.form)
        statistic_data = Statistic(
                                weekdays = weekday_now,
                                # counter = request.form['did_it'],
                                task_id=request.form['result'],
                                register_id=current_user.id
                        )
        print(request.form['result'])
        print
        try:
            db.session.add(statistic_data)
            db.session.commit()
            return redirect(url_for('profile'))
        except:
            flash('Some problem with Save results, please try again!')
            return render_template('profile.html')


    return render_template('profile.html', today_tasks=today_tasks)