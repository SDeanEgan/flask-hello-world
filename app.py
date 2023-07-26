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

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect(dblink)
    cur = conn.cursor()
    
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                    Values
                    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')
    
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def select():
    conn = psycopg2.connect(dblink)
    cur = conn.cursor()
    
    cur.execute('''
                SELECT * FROM Basketball;
                ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+=f"<td>{info}</td>"
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect(dblink)
    cur = conn.cursor()
    
    cur.execute('''
                DROP TABLE Basketball;
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
