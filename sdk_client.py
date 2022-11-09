from student import Student

import student_sdk

student = Student(
    "Kindson",
    "Munonye",
    "Computer Science"
)
# print(student_sdk.add_student(student))

print(student_sdk.get_students())
