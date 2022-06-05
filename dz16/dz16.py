# Создать Flask приложение с 2-мя endpoint GET и POST

from crypt import methods
from flask import Flask, request,jsonify,abort, Response

import json

app = Flask(__name__)

database = [ 
    {
        'name': 'Dima',
        'posts': ['Post 1','Post 2','Post 3','Post 4'],
    },
    {   
        'name': 'Fedor',
        'posts': ['Post 1','Post 2'],
    },
    {   
        'name': 'Alex',
        'posts': ['Post 1','Post 2','Post 3','Post 4','Post 5'],
    },
    {   
        'name': 'John',
        'posts': ['Post 1'],
    },
]


# def write (data,filename):
#     data = json.dumps(data)
#     data = json.loads(str(data))
#     with open(filename, "w", encoding='UTF-8',) as outfile:
#     outfile.write(outfile)


@app.route('/<name>', methods = ['GET','POST'])
def author_post (name):
    if request.method == 'GET':
        for author_post in database:
            if author_post['name'] == name:
                return jsonify(author_post['posts'])
            else:
                return abort(status=404)
    elif request.method == 'POST':
        request_data = request.get_json()
        for author in database:
            if author['name'] == name:
                author['posts'].extend(request_data['posts'])
            return Response(status = 201)
        else:
            return abort(status=404)


        
    




# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'




# @app.route('/<name>')
# def hello_world(name):
#     return f'Hello: {name}'

# @app.route('/home-<int:number>', methods =['GET','POST'])
# def number(number):
#     if request.method == "GET":
#         return {"Hello":number}
#     elif request.method == "POST":
#         return request.get_json()

# from flask import Flask, request, render_template

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

