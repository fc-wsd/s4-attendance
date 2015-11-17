from datetime import datetime


# TODO
# 시간에 랜덤 변화 주기
# 로컬 타임존으로 출력하기


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
    index = 0
    for k in sorted(attendances):
        index += 1
        print("{}. {} : ".format(index, k))
        for date in attendances[k]:
            print("\t{}".format(str(date)))
        print()


def main():
    init()

    for dt in list_date_lesson:
        for person in students:
            attend(person, dt)

    print("\nWeb Service Development 4기 출석부 :")
    print('*' * 60 + '\n')
    display_students()


if __name__ == '__main__':
    main()