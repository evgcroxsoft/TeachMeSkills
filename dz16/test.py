from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about/<name>')
def about(name):
    return f'The about page {name}'