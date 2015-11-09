from datetime import datetime

# 학생 리스트
students = ['donald', 'tom', 'jack', 'july', 'kay', 'may', 'haru']


# 학생 클래스, 이름 & 최종 출석시간
class Student:
    name = None
    last_attend_date = None

    def __init__(self, name=None, last_attend_date=datetime.now()):
        self.name = name
        self.last_attend_date = last_attend_date

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __repr__(self):
        return self.name+' '+self.last_attend_date

    def get_name(self):
        return self.name

    def get_last_attend_date(self):
        return self.last_attend_date


# 학생들을 dict 로 가지고 있는 출석부 클래스
class Attendance:
    attendance = {}

    def __init__(self):
        pass

    def add(self, name):
        self.attendance[name] = None

    def attend(self, name):
        if name not in self.attendance:
            print('There are no person named '+name)
        else:
            self.attendance[name] = datetime.now()
            print(name+' attends the class now.')

    def list(self):
        return [x for x in self.attendance if self.attendance[x] is not None]


# Main
attendance = Attendance()

for st in students:
    attendance.add(st)

attendance.attend('donald')
attendance.attend('jacks')
attendance.attend('tom')

print(attendance.list())