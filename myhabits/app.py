from __init__ import app
import send_email, models, database, connector, auth 
import config, routes, register_route, login_route, forget_password_route, change_password, profile
'''
if __name__ == '__main__':
    app.run(debug=True)
'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)