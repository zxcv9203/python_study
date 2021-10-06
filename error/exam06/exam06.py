school = {"1반" : [172, 175, 188, 199], "2반": [188,156,176]}
try:
	for class_number, students in school.items():
		for student in students:
			if student > 190:
				print(class_number, "에 190을 넘는 학생이 있습니다.")
				raise StopIteration
except StopIteration:
    print("정상종료")