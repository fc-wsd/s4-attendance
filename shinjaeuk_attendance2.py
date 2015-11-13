import time
from datetime import datetime

class Attendance:

	lateHour = 9

	students = []

	def attend(self, student):

		if( self.isLate()):
			student.isLate = True

		else:
			student.isLate = False

		student.attendanceDateTime = datetime.today()
		self.students.append(student)

	def getNumberOfStudents():
		return len(students)

	def isLate(self):

		current_hour = time.localtime()[3]

		return current_hour >= self.lateHour

	def getStudents(self):

		return self.students

	def getLateStudent(self):

		lateStudents = []

		for student in self.students:
			if( student.isLate ):
				print(student)
				lateStudents.append(student)
		
		return lateStudents

class Student:

	isLate = None

	attendanceDateTime = None

	def __init__(self, name):
		self.name = name

	def getisLate(self):
		if( self.isLate):
			return '지각'
		else:
			return '출석'

	def getAttendanceDateTime(self):
		return str(self.attendanceDateTime.month) +'월 ' + str(self.attendanceDateTime.day)  +'일 ' + str(self.attendanceDateTime.hour) +'시 ' + str(self.attendanceDateTime.minute) +'분'

	def toString(self):
		print('이름 :'+self.name)
		print('출석 시간 :'+str(self.getAttendanceDateTime()))
		print('지각여부 :'+ str(self.getisLate()))
		


attendance = Attendance()

# 출석
attendance.attend(Student('김상범'))
attendance.attend(Student('유주봉'))
attendance.attend(Student('장창완'))
attendance.attend(Student('이은상'))
attendance.attend(Student('김용열'))
attendance.attend(Student('권용현'))
attendance.attend(Student('유동균'))
attendance.attend(Student('백인기'))


# 모든 학생
print('01. 출석 리스트:')
students = attendance.getStudents()

for student in students:
	student.toString()
	print('')

# 지각생만
print('02.지각생 리스트:')
lateStudents = attendance.getLateStudent()

for student in lateStudents:
	student.toString()
	print('')
