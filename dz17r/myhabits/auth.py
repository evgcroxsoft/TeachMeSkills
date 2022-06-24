from models import Register
from __init__ import app
from flask_login import LoginManager

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Register.query.get(str(user_id))



