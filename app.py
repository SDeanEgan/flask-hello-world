from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lab10_znny_user:g1xbejQFLSESrltdvYxI90SvV5riHQDq@dpg-cj0ki9j438irjje04i3g-a/lab10_znny")
    conn.close()
    return "Database Connection Successful" 