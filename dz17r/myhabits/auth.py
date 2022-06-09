from uuid import uuid4
from models import Register
from __init__ import app
from flask_login import LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# class UserLogin():
#     def fromDB(self,user_id):
#         '''Метод который выгружает нам '''
#         self.__user = getUser(user_id)

#     def create(self, user):
#         self.__user = user
#         return self


#     def is_authenticated(self):
#         return True
    
#     def is_active(self):
#         return True

#     def is_anonymouse(self):
#         return False

#     def get_id(self):
#         return str(self.__user['id'])


# def getUser(user_id):
#     '''С базы данных выбирает ID пользователя'''
#     try:
#         user_check = Register.query.get(user_id)
#         id = user_check
#         if not id:
#             print('User not found')
#             return False
#         return id
#     except:
#         print('ERROORRRR')
#     return False

# @login_manager.user_loader
# def load_user(user_id):
#     print('HELLOO',user_id)
#     print('Load User')
#     return UserLogin().fromDB(user_id)

@login_manager.user_loader
def load_user(user_id):
    return Register.query.get(str(user_id))



