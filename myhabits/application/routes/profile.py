import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.sql import func
from application import app, db
from application.models import Task, Habit, Statistic


@app.route('/profile', methods=('GET','POST'))
@login_required
def profile():
    tasks = db.session.query(Task, Habit).filter_by(user_id=current_user.id).join(Habit).all()
    date_now = datetime.date.today()
    weekday_now = datetime.datetime.today().strftime('%A')
    ids = []
    for task, habit in tasks:
        static_game = Statistic.query.filter_by(task_id=task.id).with_entities(func.sum(Statistic.life).label('total')).first().total
        if static_game != None:
            Task.query.get(task.id).total_lifes = task.life - static_game
            db.session.commit()
        static = Statistic.query.filter_by(task_id = task.id).filter_by(created = date_now).first()
        if static == None or static.life == 1:
            if task.start_period <= date_now:
                for day in task.weekdays:
                    if day == weekday_now:
                        ids.append(task.id)
                        if static_game != None and task.life - static_game == 0:
                            Statistic.query.get(task.id).status = 'game over'
                            db.session.commit()
                        if static == None or static.task_id != task.id and static.created != date_now:
                            statistic_data = Statistic(
                                    weekdays = weekday_now,
                                    task_id = task.id,
                                    user_id = current_user.id,
                                    status = 'in process'
                                    )
                            try:
                                db.session.add(statistic_data)
                                db.session.commit()
                            except:
                                flash('Some problem with update!!!, please try again!')
                                db.session.rollback()   
    today_tasks = db.session.query(Task, Habit).filter(Task.id.in_(ids)).join(Habit).all()
    if request.method == 'POST':
        data = request.form
        dynamic_form = data.getlist('result')
        for id in dynamic_form:
            task_done = Statistic.query.filter_by(task_id = id).filter_by(created = date_now).first()
            task_done.life = 0
            counter = Statistic.query.filter_by(task_id = id).filter_by(life = 0).count()
            Task.query.get(id).remain = counter
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash('Some problem with Save results, please try again!')
                return render_template('profile.html')
        return redirect(url_for('profile'))
    total_habits_for_today = len(ids)

    return render_template('profile.html', today_tasks=today_tasks, total_habits_for_today = total_habits_for_today)