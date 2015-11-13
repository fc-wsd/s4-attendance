# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

class Student(object):
	def __init__(self, name):
		self.name = name

class Attendance(object):
	attendance = {}
	def attend(self, name):
		if name in students:
			self.attendance[name] = datetime.now()
		else:
			print ("음, 명단에 없는데요?")

	def list(self):
		for name in self.attendance:
			print ("이름: {}, 출석일자: {}".format(name, self.attendance[name]))


# 전체 학생 명단
students = ["이은상", "사명구", "정회웅", "김용열", "이준범", "김상범", "박순우", "권용현", "황준식", "백인기", "최원석", "유주봉", "신재욱", "장창완", "김주욱", "유동균"