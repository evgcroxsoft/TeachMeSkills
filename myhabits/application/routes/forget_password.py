from flask import redirect, render_template, request, flash, url_for
from application import app
from task_celery import forget_send_email
from application.models import User

@app.route('/forget_password', methods=('GET', 'POST'))
def forget_password():
    if request.method == 'POST':
        email = request.form['form_email']

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('User not found')
            return redirect(url_for('forget_password'))

        user_url = ('http://'+request.host+'/change_password'+(f'/{user.id}'))
        forget_send_email(user.email, user_url).delay()
        redirect(url_for('login'))

    return render_template('forget_password.html')