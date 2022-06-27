from flask import request, flash, redirect, url_for, render_template
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash
from __init__ import app
from models import User

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['form_email']
        password = request.form['form_password']
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('User not found')
            return render_template('login.html')

        if check_password_hash(user.password, password):
            login_user(user, remember=remember)
            return redirect(url_for('profile'))
        else: 
            flash('Wrong passport')
            return render_template('login.html')

    return render_template('login.html')