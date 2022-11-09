import sqlite3
from flask import *
import json
from student import Student

app = Flask(__name__)

def go_home():
    c = sqlite3.connect("../BookSDKDemo/book.db").cursor()
    c.execute("CREATE TABLE IF NOT EXISTS STUDENTS("
              "id TEXT, firstname TEXT, lastname TEXT, department TEXT)"
              )
    c.connection.close()


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Students API!'


@app.route('/getStudents', methods=['GET'])
def get_students():
    c = sqlite3.connect("../BookSDKDemo/book.db").cursor()
    c.execute("SELECT * FROM STUDENTS")
    data = c.fetchall()
    return jsonify(data)


@app.route('/getStudentById/<student_id>', methods=['GET'])
def get_student_by_id(student_id):
    c = sqlite3.connect("../BookSDKDemo/book.db").cursor()
    c.execute("SELECT * FROM STUDENTS WHERE id=?", (student_id,))
    data = c.fetchone()
    return json.dumps(data)


@app.route('/addStudent', methods=['POST', 'GET'])
def add_student():
    db = sqlite3.connect("../BookSDKDemo/book.db")
    c = db.cursor()
    student = Student(request.form["firstname"],
                      request.form["lastname"],
                      request.form["department"]
                      )
    print(student)
    c.execute("INSERT INTO STUDENTS VALUES(?,?,?,?)",
              (student.id, student.firstname, student.lastname, student.department))
    db.commit()
    data = c.lastrowid
    return json.dumps(data)


@app.route('/updateStudent/<student_id>', methods=['PUT'])
def update_student(student_id):
    db = sqlite3.connect("../BookSDKDemo/book.db")
    c = db.cursor()
    student = Student(request.form["firstname"],
                      request.form["lastname"],
                      request.form["department"]
                      )
    print(student)
    c.execute("UPDATE STUDENTS SET firstname = ?, lastname =?, department =? WHERE id=?",
              (student.firstname, student.lastname, student.department, student_id))
    db.commit()
    return json.dumps("Record was successfully updated")


@app.route('/deleteStudent/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    db = sqlite3.connect("../BookSDKDemo/book.db")
    c = db.cursor()
    c.execute("DELETE FROM STUDENTS WHERE id=?", (student_id,))
    db.commit()
    return json.dumps("Record was successfully deleted")

if __name__ == '__main__':
    app.run(port=8888)
