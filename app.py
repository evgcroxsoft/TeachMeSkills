from flask import Flask
from flask_crontab import Crontab

app = Flask(__name__)
crontab = Crontab(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@crontab.job(minute='1')
def google():
    print('PRIVET VSEM')

google()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')