from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from flask_login import UserMixin, LoginManager
import bcrypt
from flask import render_template, request, url_for, redirect
from flask_login import login_required, logout_user
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy_utils import database_exists, create_database, drop_database


def get_env_variable(name):
    '''Give message if some of value couln't downloaded'''
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected environment variable {name} not set."
        raise Exception(message)

POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db = SQLAlchemy(app)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next=' + request.url)
    return response

class Events(db.Model):
    # __table_args__ = {'extend_existing': True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(150), unique=False, nullable=True)
    date = db.Column(db.Date, unique=False, nullable=True)
    place = db.Column(db.String(200), unique=False, nullable=True)
    url = db.Column(db.String, unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=True)
    date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Users(db.Model, UserMixin):
    # __table_args__ = {'extend_existing': True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(50), unique=True, nullable=True)
    hash = db.Column(db.Text, unique=False, nullable=True)
    name = db.Column(db.String(150), unique=False, nullable=True)
    surname = db.Column(db.String(150), unique=False, nullable=True)
    birthday = db.Column(db.Date, unique=False, nullable=True)
    address = db.Column(db.String(200), unique=False, nullable=True)
    date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())

@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')


# resetdb_command()

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    print("load_user")
    return Users.query.get(id)

@app.route('/create_event/', methods=('GET', 'POST'))
@login_required
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
@login_required
def index():
    events_table = Events.query.order_by(Events.date_added.desc()).all()
    return render_template('index.html', events_table=events_table)

@app.route('/user')
@login_required
def user():
    users_table = Users.query.order_by(Users.date_added.desc()).all()
    return render_template('user.html', users_table=users_table)

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
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        string_password = hashed.decode('utf-8')
        print(string_password)

        user = Users(
                    email=email, 
                    hash=string_password,
                    name=name, 
                    surname=surname, 
                    birthday=birthday, 
                    address=address
                    )

        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            message = 'Some problem with registration, please try again!'
            return render_template('register.html', message=message)
        
    return render_template('register.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'] 
        
        user = Users.query.filter_by(email=email).first()
        # flash('Test')
        if not user:
            message = 'User not found'
            return render_template('login.html', message=message)

        if bcrypt.checkpw(password.encode('utf-8'), f"{user.hash}".encode('utf-8')):

            next_page = request.args.get('next')

            return redirect(next_page)
        else: 
            message = 'Wrong passport'
            return render_template('login.html', message=message)

    return render_template('login.html')


@app.route('/logout', methods=('GET', 'POST'))
@login_required
def logout():
    logout_user()
    return redirect(url_for('create_event'))

# @app.after_request
# def redirect_to_signin(response):
#     if response.status_code == 401:
#         return redirect(url_for('login') + '?next=' + request.url)
#     return response

