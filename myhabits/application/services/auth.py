from flask_login import LoginManager
from application import app
from application.models import User

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))
