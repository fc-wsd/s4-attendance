# coding: utf-8

from datetime import datetime 

students = [
    '장창완', '이준범', '박순우', '김상범',
    '김용열', '정의석', '유주봉', '최원석',
    '김주욱', '황정식', '권용현', '유동균'
    ]

attendances = {}

def attend(name):
    if name not in students:
        print("{0}: 명단에 있는 학생이 아닙니다.".format(name))
        return
    attendances[name] = datetime.now()

def printAttendances():
    print("------------------")
    for name, date in attendances.items():
        print("{0} : {1}".format(name, date))
    print("------------------")


printAttendances()
print("")

attend('차경목')
print("")
attend('김용열')
attend('이준범')

printAttendances()

