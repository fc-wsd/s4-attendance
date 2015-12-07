#coding: utf8

from datetime import datetime
import time

# 학생 명단이 있는 객체 `students` 명단
# Sublime Text 3 에서 build시 UnicodeEncodeError 가 발생하여, 일단은 영어로 작성
students = ["김용열", "김상범", "박순우", "이준범", "정회웅", "황준식"]
# students = ["Yongyeol", "Sangbeom", "Soonwoo", "Junbeom", "Hoiwoong", "Junsik"]

# 출석자는 `attendances` 객체에 저장하며, 출석 일시와 이름은 필수 저장 항목.
attendances = {}

# `attend()` 함수로 출석 처리.
def attend(student):
    if student in students:
        attendances[student] = getTimeStamp()
        return True
    else:
        return False

def getTimeStamp():
    d = datetime.now().isoformat()
    # time.sleep(1) # for checking timestamp
    return d[0:10] + ' ' + d[11:19]

# test
for student in students:
    attend(student)

print (attendances)