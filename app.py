from flask import Flask
import psycopg2

app = Flask(__name__)

dblink = "postgres://lab10_znny_user:g1xbejQFLSESrltdvYxI90SvV5riHQDq@dpg-cj0ki9j438irjje04i3g-a/lab10_znny"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect(dblink)
    conn.close()
    return "Database Connection Successful" 

@app.route('/db_create')
def create():
    conn = psycopg2.connect(dblink)
    cur = conn.cursor()
    
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Basketball(
                    First varchar(255),
                    Last varchar(255),
                    City varchar(255),
                    Name varchar(255),
                    Number int
                    );
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Added Successfully"