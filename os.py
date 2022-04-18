# Функции модуля ОС
import os

print(os.name)

for key in os.environ:
    print (key,':',os.environ[key])

for value in os.environ.items():
    print(value)

print(os.environ['TMS'])
password = os.getenv('TMS')
print(password)

#os.remove('bla.py')
print(os.path.exists('/home/python/Desktop/Python course/TeachMeSkills/dz11.py'))

print(os.path.exists('/home/python/Desktop/Python course/TeachMeSkills/My_own_helper.py'))