# import bcrypt
# from flask import render_template, request, url_for, redirect
# from flask_login import login_required, logout_user
# from sky import app, db
# from sky.models import Events, Users


# @app.route('/create_event/', methods=('GET', 'POST'))
# @login_required
# def create_event():
#     if request.method == 'POST':
#         name = request.form['name']
#         date = request.form['date']
#         place = request.form['place']
#         url = request.form['url']
#         description = request.form['description']

#         create_event = Events (
#                         name=name, 
#                         date=date, 
#                         place=place, 
#                         url=url, 
#                         description=description
#                         )
        
#         try:
#             db.session.add(create_event)
#             db.session.commit()
#             return redirect(url_for('index'))
#         except:
#             return '<h1>Some problem with new event</h1>'

#     return render_template('create_event.html')

# @app.route('/')
# @login_required
# def index():
#     events_table = Events.query.order_by(Events.date_added.desc()).all()
#     return render_template('index.html', events_table=events_table)

# @app.route('/user')
# @login_required
# def user():
#     users_table = Users.query.order_by(Users.date_added.desc()).all()
#     return render_template('user.html', users_table=users_table)

# @app.route('/register/', methods=('GET', 'POST'))
# def register():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         name = request.form['name']
#         surname = request.form['surname']
#         birthday = request.form['birthday']
#         address = request.form['address']

#         repeat_password = request.form['repeat_password']
#         user_check = Users.query.filter_by(email=email).first()

#         if password != repeat_password:
#             message = 'Different passwords'
#             return render_template('register.html',message=message)
        
#         if email == user_check:
#             message = 'Such Email already exists'
#             return render_template('register.html',message=message)
        
#         hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#         string_password = hashed.decode('utf-8')
#         print(string_password)

#         user = Users(
#                     email=email, 
#                     hash=string_password,
#                     name=name, 
#                     surname=surname, 
#                     birthday=birthday, 
#                     address=address
#                     )

#         try:
#             db.session.add(user)
#             db.session.commit()
#             return redirect(url_for('login'))
#         except:
#             message = 'Some problem with registration, please try again!'
#             return render_template('register.html', message=message)
        
#     return render_template('register.html')


# @app.route('/login', methods=('GET', 'POST'))
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password'] 
        
#         user = Users.query.filter_by(email=email).first()
#         # flash('Test')
#         if not user:
#             message = 'User not found'
#             return render_template('login.html', message=message)

#         if bcrypt.checkpw(password.encode('utf-8'), f"{user.hash}".encode('utf-8')):

#             next_page = request.args.get('next')

#             return redirect(next_page)
#         else: 
#             message = 'Wrong passport'
#             return render_template('login.html', message=message)

#     return render_template('login.html')


# @app.route('/logout', methods=('GET', 'POST'))
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('create_event'))

# @app.after_request
# def redirect_to_signin(response):
#     if response.status_code == 401:
#         return redirect(url_for('login') + '?next=' + request.url)
#     return response

# if __name__ == "main":
#     app.run(debug=True)

