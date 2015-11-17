from pprint import pprint
from datetime import datetime


# 전체 학생 명단
students = (
    'Dennis Ingi Baek',
    'Jungsik Whang',
    'Minjae Lee',
    'Peter Jeong',
    'Won Seok Choi',
    'Yong Hyun Kwon',
    '김상범',
    '김용열',
    '김주욱',
    '류지환',
    '박순우',
    '사명구',
    '신재욱',
    '신해동',
    '유동균',
    '유주봉',
    '이은상',
    '이준범',
    '장창완',
    '정의석',
)

list_date_lesson = [
    datetime(2015, 10, 31, 13, 0, 0),
    datetime(2015, 11, 7, 13, 0, 0),
    datetime(2015, 11, 14, 13, 0, 0),
]


attendances = {}

# 출석자 이름과 출석일시를 필수로 저장
def init():
    for name in students:
        attendances[name] = []


def attend(name, time):
    attendances[name].append(time)

def display_students():
    for k in sorted(attendances):
        print("{} : ".format(k), end="")
        for date in attendances[k]:
            print("{}".format(str(date)), end=" / ")
        print()


def main():
    init()
    for dt in list_date_lesson:
        for person in students:
            attend(person, dt)

    print("Web Service Development 4기 명단 :")
    display_students()


if __name__ == '__main__':
    main()