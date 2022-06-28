from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db, app
from app.models import User

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