from flask import Flask
import mysql.connector

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

mysql = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='toor',
    database='delivery'
)

from app.routes import routes