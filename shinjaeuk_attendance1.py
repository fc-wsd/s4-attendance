students = ['김상범', '유주봉', '장창완', '이은상', '김용열', '권용현', '유동균', '백인기']

attendance = []

def attend(student):
	attendance.append(student)

#출석
for student in students:
	attend(student)

#출석확인
for student in attendance:
	print(student)