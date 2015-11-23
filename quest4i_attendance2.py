from datetime import datetime
import random


class Student(object):

    def __init__(self, name, display_name=None):
        self.name = name
        self.display_name = display_name

    def __str__(self):
        if self.display_name is not None:
            print("Name = {} : Display Name : {}".format(self.name, self.display_name))
        else:
            print("Name = {}".format(self.name))




class Attendance:

    def __init__(self, date):
        self.date = date
        self.students = []

    def attend(self, student):
        self.students.append(student)

    def list(self):

        print("출석부 ({})".format(self.date))
        for st in self.students:
            print("{}. {}".format(self.students.index(st), st.name))

        print("*" * 30)
        print("")



LIST_DATE_LESSON = [
    datetime(2015, 10, 31, 13, 0, 0),
    datetime(2015, 11, 7, 13, 0, 0),
    datetime(2015, 11, 14, 13, 0, 0),
    datetime(2015, 11, 21, 13, 0, 0),
]


def main():

    students = [
        Student('dennisbaek'),
        Student('elee7812'),
        Student('hannal', 'Kay Cha'),
        Student('heyyjude'),
        Student('iamsolucky'),
        Student('jangchan'),
        Student('junkwhinger'),
        Student('PeppyDays'),
        Student('perterjeong'),
        Student('plusbeauxjours'),
        Student('quest4i', 'Myeonggu Sa'),
        Student('sagan9', 'Sangbeom Kim'),
        Student('shinjaeuk', 'Shin Jaeuk'),
        Student('silversky112', 'Wonseok Choi'),
        Student('sunu-park', 'Sunu Park'),
        Student('Vereco'),
        Student('wwwjb')
    ]
    print("")
    print("학생 명단 -----")
    for st in students:
        # print("{}. name = {} : display name = {}".format(students.index(st), st.name, st.display_name))
        if st.display_name:
            print("{}. {} ({})".format(students.index(st), st.name, st.display_name))
        else:
            print("{}. {}".format(students.index(st), st.name))
    print("\n\n\n")

    list_attendance = []
    index = 0
    for dt in LIST_DATE_LESSON:
        list_attendance.append(Attendance(dt.date()))
        user_number = random.randrange(1, 18)
        random.shuffle(students)
        for i in range(user_number+1):
            list_attendance[index].attend(students[i])

        index += 1

    print("")
    print("출석부 ----")
    for at in list_attendance:
        at.list()


if __name__ == '__main__':
    main()