from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])




CREATE DATABASE flask_db;
CREATE USER zhenya WITH PASSWORD '`b{5:P3kUv5LdJF.';
GRANT ALL PRIVILEGES ON DATABASE flask_db TO zhenya;
\l
\q
pip install Flask psycopg2-binary
sudo -iu postgres psql
\c flask_db
SELECT title, author FROM books;
\q

source dz17r/.env