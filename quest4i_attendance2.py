from datetime import datetime
from pprint import pprint


class Student:

    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name

    def __init__(self, name):
        self.name = name

    def __str__(self):
        print("{} : {}".format(self.name, self.display_name))



class Attendance:

    def __init__(self):
        self.students = []

    def attend(self, student):
        self.students.append(student)

    def list(self):
        pprint(self.students)



LIST_DATE_LESSON = [
    datetime(2015, 10, 31, 13, 0, 0),
    datetime(2015, 11, 7, 13, 0, 0),
    datetime(2015, 11, 14, 13, 0, 0),
    datetime(2015, 11, 21, 13, 0, 0),
]


#
# # 출석자 이름과 출석일시를 필수로 저장
# def init():
#     for name in students:
#         attendances[name] = []
#
#
# def attend(name, time):
#     attendances[name].append(time)
#
#
# def display_students():
#     index = 0
#     for k in sorted(attendances):
#         index += 1
#         print("{}. {} : ".format(index, k))
#         for date in attendances[k]:
#             print("\t{}".format(str(date)))
#         print()


def main():

    students = [
        Student('dennisbaek')
    ]

    pprint(students[0])




if __name__ == '__main__':
    main()