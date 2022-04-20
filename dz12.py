# Создать  и активировать  виртуальное окружение
'''
python3 -m venv venv
source venv/bin/activate
deactivate
'''
# Добавить название вашего виртуального окружения venv в  исключения .gitignore
'''
Добавилено название .venv/ в .gitignore
'''
# Создать пакет Python добавить стороннюю библиотеку
'''
Скачал django, fastapi. 
Использовал команды 
pip list
pip install
pip unistall
pip list | grap fastapi
'''
# Загрузить пакет на Pypi
'''
Статья полезная с описанием действий.
https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3

Мой пакет залитый на Pypi
С первого раза не залился, так имя такое уже существовало, пришлось изменять имя в фале setup.py 
и после заного создавать dist.

pip install Guess-my-number-EVG==0.1

'''

# Почитать про PEP8 и PEP20