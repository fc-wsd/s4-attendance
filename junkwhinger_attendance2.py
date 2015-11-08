#coding: utf-8

from datetime import datetime

students = ['황준식','김상범','사명구','김주욱']

class Student(object):

	def __init__(self, name):
		self.name = name
		self.when = None
		self.attended = False


class Attendance(object):

	def __init__(self, name):
		self.name = name
		self.attended_students = []

	def attend(self, Student):
		Student.attended = True
		Student.when = datetime.now()
		self.attended_students.append(Student)

	def list(self):
		num_of_students = len(self.attended_students)
		print ('%d student(s) in the class.' %num_of_students)
		for student in self.attended_students:
			print ('{} attended at {}'.format(student.name, student.when.strftime("%H:%M:%S")))