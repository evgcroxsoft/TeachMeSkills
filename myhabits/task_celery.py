from flask_mail import Message
from flask import flash 
from application.services.flask_celery import celery, logger
from application.models import User
from application.services.check_task import task_check
from application import mail

@celery.task(name ="periodic_task")
def periodic_task():
    for user in User.query.all():
        task_check(user.id)
        logger.info(f"Periodic task, {user.id}")

@celery.task()
def send_email(email):
    msg = Message('MyHabits')
    msg.recipients = [f'{email}']
    msg.body = 'You have been registered successfully! Please, activate your email!'
    mail.send(msg)
    logger.info(f"Sended email, {email}")
    return flash('Please activate your email', category = 'succsess')


@celery.task()
def forget_send_email(email, user_url):
    msg = Message('MyHabits')
    msg.recipients = [f'{email}']
    msg.body = f'Please follow to the link to change your password: {user_url}!'
    mail.send(msg)
    logger.info(f"Sended email, {email}")
    return flash('Check your email!')