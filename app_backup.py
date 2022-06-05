import bcrypt
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from pkg_resources import register_namespace_handler
from db_app import app, db, DB_URL, get_env_variable, Events, Users, resetdb_command

# resetdb_command()
@app.route('/create_event/', methods=('GET', 'POST'))
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        place = request.form['place']
        url = request.form['url']
        description = request.form['description']

        create_event = Events (
                        name=name, 
                        date=date, 
                        place=place, 
                        url=url, 
                        description=description
                        )
        
        try:
            db.session.add(create_event)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return '<h1>Some problem with new event</h1>'

    return render_template('create_event.html')


@app.route('/')
def index():
    events_table = Events.query.all()
    return render_template('index.html', events_table=events_table)

@app.route('/user')
def user():
    users_table = Users.query.order_by(Users.date_added)
    return render_template('user.html', users_table=users_table)

# @app.route('/<name>', methods = ['GET','POST'])
# def author_post (name):
#     if request.method == 'GET':
#         for user in Users:
#             if user['name'] == name:
#                 return redirect(url_for('index'))



@app.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        surname = request.form['surname']
        birthday = request.form['birthday']
        address = request.form['address']

        repeat_password = request.form['repeat_password']
        user_check = Users.query.filter_by(email=email).first()

        if password != repeat_password:
            message = 'Different passwords'
            return render_template('register.html',message=message)
        
        if email == user_check:
            message = 'Such Email already exists'
            return render_template('register.html',message=message)
        
        hashed = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        register = Users(
                    email=email, 
                    password=hashed,
                    name=name, 
                    surname=surname, 
                    birthday=birthday, 
                    address=address
                    )

        try:
            db.session.add(register)
            db.session.commit()
            return redirect(url_for('user'))
        except:
            message = 'Some problem with registration, please try again!'
            return render_template('register.html', message=message)
    
    return render_template('register.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    
        email_check = Users.query.filter_by(email=email).first()

        if not email_check:
            message = 'User not found'
            return render_template('login.html', message=message)
        
        if bcrypt.checkpw(password.encode('utf-8'), Users.password):
            print('All Ok')
            message = 'Wrong passport'
            return redirect(url_for('index'))
        else: 
            return render_template('login.html', message=message)

    
    return render_template('login.html')