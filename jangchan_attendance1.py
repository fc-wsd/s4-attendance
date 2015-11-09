# coding: utf-8

#import datetime
from datetime import *


students = ['장창완', '이준범', '박순우', '김상범', '김용열', '정의석', '유주봉', 
    '최원석', '김주욱', '황정식', '권용현', '유동균', ]

attendance = []


def attend(name):
    # 명단에 있는 학생인가?
    if name not in students:
        print("명단에 있는 학생이 아닙니다. ({})".format(name))
        return

    # 출석부에 등록
    e = name, datetime.now()
    attendance.append( e )
    
    print("출석자 등록: ({}), {}".format(e[0], e[1]))


def list():
    print()
    print("==============")
    print("=== 출석부 ===")
    print("==============")
    for e in attendance:
        print("출석: {}, {}".format(e[0], e[1]))

# main

# 출석 등록
attend('차경묵')
attend('장창완')
attend('권용현')
attend('유주봉')

# 출석 명단 출력
list()