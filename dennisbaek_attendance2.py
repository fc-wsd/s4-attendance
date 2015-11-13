
import time
from datetime import datetime



class Students:
    def __init__(self):
        self.students = [
                            '김상범',
                            '유주봉',
                            '장창완',
                            '이은상',
                            '김용열',
                            '권용현',
                            '유동균',
                            '백인기',
                            ]

class Attendance:
    attendances = {}
    def attend(self, name):
        self.attendances[name] = [
                                time.localtime().tm_hour,
                                time.localtime().tm_min,
                                time.localtime().tm_sec
                                ]
    def show_attend(self):
        return self.attendances
    def list(self):
        return list(self.attendances)

#test&basic settings
s = Students()
a = Attendance()
for i in s.students:
    a.attend(i)

a.show_attend()
a.list()
