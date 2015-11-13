# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

# 전체 학생 명단
students = ["이은상", "사명구", "정회웅", "김용열", "이준범", "김상범", "박순우", "권용현", "황준식", "백인기", "최원석", "유주봉", "신재욱", "장창완", "김주욱", "유동균"

# 오늘 수업 참가한 학생 명단과 일시
attendances = {}

def attend(student):
	if student in students:
		attendances[student] = datetime.now()
		print ("아, {}씨, 반가워요. 출석일자는 {}입니다.".format(student, attendances[student]))
	else:
		print ("음, 명단에 없는데요?")