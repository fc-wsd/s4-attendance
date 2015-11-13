from datetime import datetime

attendences = {}

def attend():
	student = input("출석자 이름: ")
	now = datetime.now()
	stamp = now.strftime('%Y-%m-%d')
	attendences[student] = stamp
	print (("이름: "), student, ("| 출석일시: "), attendences.get(student))
