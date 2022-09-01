from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from application import app, db
from application.models import Task, Habit, Statistic
from application.services.check_task import task_check
import datetime



@app.route('/profile', methods=('GET','POST'))
@login_required
def profile():
    date_now = datetime.date.today()
    ids = task_check(current_user.id)
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