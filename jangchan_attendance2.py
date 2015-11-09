# coding: utf-8

from datetime import *

class Student(object):
    def __init__(self, name):
        self.name = name

class Attendance(object):
    def __init__(self, students):
        self.students = students
        self.attendances = []

    def attend(self, student):
        # 명단에 있는 학생인가?
        if student.name not in self.students:
            print("명단에 있는 학생이 아닙니다. ({})".format(student.name))
            return

        e = (student, datetime.now())
        self.attendances.append(e)
        print("출석자 등록: ({}), {}".format(e[0].name, e[1]))

    def list(self):
        print()
        print("==============")
        print("=== 출석부 ===")
        print("==============")

        for e in self.attendances:
            print("출석: {}, {}".format(e[0].name, e[1]))

# main
students = ['장창완', '이준범', '박순우', '김상범', '김용열', '정의석', '유주봉', 
    '최원석', '김주욱', '황정식', '권용현', '유동균', ]

# 출석부 생성
attendance = Attendance(students)

# 이중에 학생이 아닌 사람이 있다
attendance.attend(Student('장창완'))
attendance.attend(Student('권용현'))
attendance.attend(Student('차경묵'))
attendance.attend(Student('유주봉'))

# 출석자 명단 출력
attendance.list()