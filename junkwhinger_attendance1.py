#coding: utf-8
from datetime import datetime

#a unique set of students
student_set = ('황준식','김상범','사명구','김주욱')

#a list of students who are present
attendances = []

#attend function
def attend(student):
	if student in student_set:
		print ('teacher: %s!' %student)
		print ('%s: yes, sir!' %student)

		now = datetime.now()
		attended_dic = dict()
		attended_dic['name'] = student
		attended_dic['attended_time'] = now
		attendances.append(attended_dic)

		print ('*' * 10)

	else:
		print ("teacher: you are not my student. get out.")

#iteration through the existing student_set
for student in student_set:
	attend(student)

number_of_attended_students = len(attendances)

def status_report():
	print ('%d students are present in the class.' % number_of_attended_students)
	for student in attendances:
		print ('{} arrived at {}'.format(student['name'], student['attended_time'].strftime("%H:%M:%S")))

#today's status report
status_report()