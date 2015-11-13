import time
from datetime import datetime

students = ['김상범',
            '유주봉',
            '장창완',
            '이은상',
            '김용열',
            '권용현',
            '유동균',
            '백인기',
            ]

attendances = {}
standard_hour, standard_min, standard_sec = 0, 0, 0

#출석 체크, 이름:시간 형태로 dict로 저장
def attend(name):
    if name in students == False:
        print('you are not in this class')
    else:
        attendances[name] = [
                        time.localtime().tm_hour,
                        time.localtime().tm_min,
                        time.localtime().tm_sec]
    return None

def show_attend():
    for i in attendances:
        print(i, attendances[i])

def show_set_time():
    print('{0}:{1}:{2} is set time!'.format(standard_hour, standard_min, standard_sec))


#기순 시간 정하기 default값으로는 set_time 함수 호출 시간
def set_time(input_hour = time.localtime().tm_hour, input_min = time.localtime().tm_min, input_sec = time.localtime().tm_sec):
    global standard_hour, standard_min, standard_sec
    standard_hour = input_hour
    standard_min = input_min
    standard_sec = input_sec
    return 'time is set'

#기준 시간에 대하여 출석 체크 된 이름별로 지각여부 체크
def late_check(name):
    if name in students == False:
        print('you are not in this class')
    elif name in attendances.keys() == False:
        print('you are never attended!')
    elif attendances[name][0] > standard_hour:
        print('{0} is late for class'.format(name))
    elif attendances[name][1] > standard_min:
        print('{0} is late for class'.format(name))
    elif attendances[name][2] > standard_sec:
        print('{0} is late for class'.format(name))
    else:
        print('{0} is on time'.format(name))

#주어진 학생 리스트 모두 지각 체크
def all_late_check(list):
    l = []
    for i in list:
        if i in attendances.keys() == False:
            print('{}! you are never attended!'.format(i))
        else:
            l = l+[late_check(i)]
    return None

#test cases!!!
'''
print('the text that is shown under here is test!!')
print('-------------------------------------------')
attend('유동균')
attend('권용현')
attend('김용열')
attend('유주봉')
attend('이은상')
attend('김상범')
attend('장창완')
attend('백인기')

'''





for i in students:
    attend(i)

for i in students[::2]:
    attend(i)
