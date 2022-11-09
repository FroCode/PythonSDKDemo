import sqlite3

from student import Student

def cursor():
    return sqlite3.connect("student.db").cursor()

c = cursor()

c.execute('CREATE TABLE IF NOT EXISTS STUDENTS(id TEXT, firstname TEXT, lastname TEXT, department TEXT)')
c.connection.close()

def add_student(student):
        c = cursor()
        with c.connection:
            c.execute('INSERT INTO STUDENTS VALUES(?, ?, ?, ?)',(student.id, student.firstname, student.lastname, student.department))
        return  c.lastrowid

def get_students():
    c = cursor()
    students = []
    with c.connection:
        for student in c.execute('SELECT * FROM STUDENTS'):
            students.append(student)
    c.connection.close()
    return students

def get_student_by_id(id):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM STUDENTS WHERE id = ?', (id,))
    data = c.fetchone()
    c.connection.close()
    if not data:
        return None
    else:
        return Student(data)

def edit_student(student):
    c = cursor()
    with c.connection:
        c.execute('UPDATE STUDENTS SET firstname = ?, lastname=?, department=? WHERE id=?',
                  (student.firstname, student.lastname, student.department, student.id))
        c.execute('SELECT changes()')

def delete_student(id):
    c = cursor()
    with c.connection:
        c.execute('DELETE * FROM STUDENTS WHERE  id=?', (id,))
    return "Record was deleted"