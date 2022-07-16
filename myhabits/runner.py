from application import app
from application.routes import about_me, change_password, forget_password, habits, login, profile
from application.routes import register, routes, tasks
from application.services import auth, send_email, session_check, utils
from application.routes import login
from application.routes import register
import task_celery as task_celery

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')