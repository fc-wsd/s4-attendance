# coding: utf-8
from datetime import datetime

#학생 명단
students = ["권용현", "김상범", "김용열", "김주욱", "박순우", "백인기", "사명구", "신재욱",
			"유동균", "유주봉", "이은상", "이준범", "장창완", "정회웅", "최원석", "황준식"]

#학생 클래스
class Student(object):
	def __init__(self, name):
		self.name = name

#출석부 클래스
class Attendance(object):
	def __init__(self):
		self.attendances = []
	#출석 처리 함수
	def attend(self, Student):
		if Student.name not in students:
			print("{}은(는) 출석부에 없는 학생입니다.".format(Student.name))
			return
		attend_log_dic = {}
		attend_log_dic["name"] = Student.name
		attend_log_dic["time"] = datetime.now()
		self.attendances.append(attend_log_dic)
		print("{}은(는) 출석하였습니다.".format(Student.name))
	#출석자 확인 함수
	def list(self):
		if len(self.attendances) == 0:
			print("출석한 사람이 아무도 없습니다.")
			return
		for student in self.attendances:
			print("이름:{} 출석일시:{}".format(student["name"], student["time"]))
