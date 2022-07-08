from app import app
from app.routes import about_me, change_password, forget_password, habits, login, profile
from app.routes import register, routes, tasks
from app.services import auth, send_email, session_check, utils
from app.routes import login
from app.routes import register

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)