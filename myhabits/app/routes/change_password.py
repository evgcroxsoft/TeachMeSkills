import re
from flask import flash, redirect, render_template, request, url_for
from app import db, app
from app.models import User
from app.services.send_email import send_email
from app.services.session_check import session_check
from werkzeug.security import generate_password_hash

@app.route('/change_password/<uuid:id>', methods=('GET', 'POST'))
def change_password(id):
    user_check = User.query.get(id)
    if id == user_check.id:
        limit_link = int(session_check())
        if limit_link < 3:
            if request.method == 'POST':
                confirmed_password = request.form['form-password']
                confirmed_password_2 = request.form['form-password_2']
                regex_password = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"

                if confirmed_password != confirmed_password_2:
                    flash('Passwords do not match', category = 'error')
                    return redirect(url_for('change_password', id=user_check.id))
                
                if len(confirmed_password) < 8:
                    flash('Password should have more than 8 characters', category='error')
                    return redirect(url_for('change_password', id=user_check.id))
                
                if re.fullmatch(regex_password, confirmed_password) == None:
                    flash('Password no Match!', category='error')
                    return redirect(url_for('change_password', id=user_check.id))
                    
                hashed_password = generate_password_hash(confirmed_password)
                user_check.password = hashed_password
                try:
                    db.session.commit()
                    send_email(user_check.email)
                    return redirect(url_for('login'))
                except Exception:
                    flash('Some problem with registration, please try again!')
                    return render_template('change_password.html')
        else:
            flash(f'You have already used this link, please try login in or push Forget password again!')
            return redirect(url_for('login'))
    return render_template('change_password.html', id=user_check.id)
