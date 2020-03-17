import os
from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy # 是个框架


app = Flask(__name__)
db=pymysql.connect("localhost", 'root', '', 'spring')
cursor = db.cursor()
cursor.execute("select * from account")
data = list(cursor.fetchall())


@app.route('/')
def index():
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)