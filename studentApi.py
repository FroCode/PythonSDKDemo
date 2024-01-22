import sqlite3
from flask import *
import json
from student import Student

App_ = Flask(__name__)

def go_home():
    c = sqlite3.connect("../BookSDKDemo/book.db").cursor()
    c.execute("CREATE TABLE IF NOT EXISTS STUDENTS("
              "id TEXT, firstname TEXT, lastname TEXT, department TEXT)"
              )
    c.connection.close()

