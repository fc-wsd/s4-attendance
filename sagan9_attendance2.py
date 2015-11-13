#coding: utf8

from datetime import datetime
import time

# 학생 명단이 있는 객체 `students` 명단
# Sublime Text 3 에서 build시 UnicodeEncodeError 가 발생하여, 일단은 영어로 작성
# students = ["김용열", "김상범", "박순우", "이준범", "정회웅", "황준식"]
students = ["Yongyeol", "Sangbeom", "Soonwoo", "Junbeom", "Hoiwoong", "Junsik"]

# Student Class
class Student(object):
    def __init__(self, name):
        self.name = name

# Attendance Class
class Attendance(object):
    def __init__(self):
        self.attendances = {}
    def attend(self, Student):
        if Student.name in students:
            self.attendances[Student.name] = self.getTimeStamp()
            return True
        else:
            return False
    def list(self):
        print('----- current:', self.getTimeStamp(), '-----')
        for entry in self.attendances:
            print(entry, 'attended on', self.attendances[entry])
        print('----- end of list -----')
    # helper function for making timestamp
    def getTimeStamp(self):
        d = datetime.now().isoformat()
        # time.sleep(1) # for checking timestamp
        return d[0:10] + ' ' + d[11:19]

# test
yy = Student(students[0])
sb = Student(students[1])
sw = Student(students[2])
jb = Student(students[3])
hw = Student(students[4])
js = Student(students[5])

print(sb.name)

attendance = Attendance()
attendance.attend(yy)
attendance.attend(sb)
attendance.list()
time.sleep(1)

attendance.attend(sw)
attendance.attend(jb)
attendance.attend(hw)
attendance.attend(js)
time.sleep(1)
attendance.list()
