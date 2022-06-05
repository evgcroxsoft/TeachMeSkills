# https://pythonhosted.org/Flask-Mail/
import os
from __init__ import app
from flask_mail import Mail, Message
from flask import flash 

app.config['TESTING'] = False
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = 'myhabits@croxsoft.com'
app.config['MAIL_MAX_EMAILS'] = None 
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATACHMENTS'] = False

mail = Mail(app)

# @app.route('/email')
# def e_mail():
#     list = ['lalalend4321@gmail.com', 'pangenya321@icloud.com']
#     for i in list:
#         msg = Message('My habits online')
#         print(i)
#         msg.recipients = [f'{i}']
#         msg.body = 'Hello, I am an automatic system'
#         mail.send(msg)
#     return 'Message has been sent!'

def send_email(form_email):
    msg = Message('MyHabits')
    msg.recipients = [f'{form_email}']
    msg.body = 'You have been registered successfully! Please, activate your email!'
    mail.send(msg)
    return flash('Please activate your email', category = 'succsess')

def forget_send_email(form_email, user_url):
    msg = Message('MyHabits')
    msg.recipients = [f'{form_email}']
    msg.body = f'Please follow to the link to change your password: {user_url}!'
    mail.send(msg)
    return flash('Check your email!')