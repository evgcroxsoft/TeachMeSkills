# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from sqlalchemy.sql import func
# from flask_login import UserMixin, LoginManager
# from sky.app import db, app, DB_URL

# class Events(db.Model):
#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = db.Column(db.String(150), unique=False, nullable=True)
#     date = db.Column(db.Date, unique=False, nullable=True)
#     place = db.Column(db.String(200), unique=False, nullable=True)
#     url = db.Column(db.String, unique=False, nullable=True)
#     description = db.Column(db.Text, unique=False, nullable=True)
#     date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())

# class Users(db.Model, UserMixin):
#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     email = db.Column(db.String(50), unique=True, nullable=True)
#     hash = db.Column(db.Text, unique=False, nullable=True)
#     name = db.Column(db.String(150), unique=False, nullable=True)
#     surname = db.Column(db.String(150), unique=False, nullable=True)
#     birthday = db.Column(db.Date, unique=False, nullable=True)
#     address = db.Column(db.String(200), unique=False, nullable=True)
#     date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())



# login_manager = LoginManager(app)

# @login_manager.user_loader
# def load_user(user_id):
#     print("load_user")
#     return Users.query.get(user_id)


# from sqlalchemy_utils import database_exists, create_database, drop_database

# @app.cli.command('resetdb')
# def resetdb_command():
#     """Destroys and creates the database + tables."""

#     if database_exists(DB_URL):
#         print('Deleting database.')
#         drop_database(DB_URL)
#     if not database_exists(DB_URL):
#         print('Creating database.')
#         create_database(DB_URL)

#     print('Creating tables.')
#     db.create_all()
#     print('Shiny!')


class Connect_to_bd():
    def __init__(self, POSTGRES_URL, POSTGRES_USER, POSTGRES_PW, POSTGRES_DB):
        self.POSTGRES_URL = POSTGRES_URL
        self.POSTGRES_USER = POSTGRES_USER
        self.POSTGRES_PW = POSTGRES_PW
        self.POSTGRES_DB = POSTGRES_DB
    
    def get_env_variable(self,name):
        '''Give message if some of value couln't downloaded'''
        try:
            return os.environ[name]
        except KeyError:
            message = f"Expected environment variable {name} not set."
        raise Exception(message)

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")

connect_object = Connect_to_bd (url,user,pw,db)











