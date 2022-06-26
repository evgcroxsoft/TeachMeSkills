from send_email import forget_send_email
from __init__ import app
from flask import redirect, render_template, request, flash, url_for
from models import Register

@app.route('/forget_password', methods=('GET', 'POST'))
def forget_password():
    if request.method == 'POST':
        form_email = request.form['form_email']

        check_user = Register.query.filter_by(email=form_email).first()

        if not check_user:
            flash('User not found')
            return redirect(url_for('forget_password'))

        user_url = ('http://'+request.host+'/change_password'+(f'/{check_user.id}'))
        email = check_user.email
        forget_send_email(email, user_url)
        redirect(url_for('login'))

    return render_template('forget_password.html')