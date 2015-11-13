# coding: utf-8

from datetime import datetime 



class Student(object):
    def __init__(self, name):
        self.name = name

class Attendance(object):
    students = [
        '장창완', '이준범', '박순우', '김상범',
        '김용열', '정의석', '유주봉', '최원석',
        '김주욱', '황정식', '권용현', '유동균'
        ]
    def __init__(self):
        self.attendances = {}

    def attend(self, student):
        if student.name not in Attendance.students:
            print("{0}: 명단에 있는 학생이 아닙니다.".format(student.name))
            return
        self.attendances[student.name] = datetime.now()

    def printAttendances(self):
        print("-----------------------")
        for name, date in self.attendances.items():
            print("{0} : {1}".format(name, date))
        print("-----------------------")



attendance = Attendance()
attendance.printAttendances()

print("")
student1 = Student('차경목')
student2 = Student('김용열')
student3 = Student('이준범')

attendance.attend(student1)
print("")
attendance.attend(student2)
attendance.attend(student3)

attendance.printAttendances()

