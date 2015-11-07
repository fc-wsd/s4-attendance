# 출석부 만들기1, vereco_attendance1.py

from datetime import datetime

students = {
    "이준범": None,
    "Peter": None,
    "김상범": None,
    "Sunu": None,
}

def attend(name):
    if name in students:
        students[name] = datetime.now()
        return
    else:
        print("등록되지 않은 수강생입니다.")
        return
