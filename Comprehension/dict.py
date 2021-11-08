students = ["yongckim", "yongcpark", "yongclee"]
for number, name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number, name))
    
std_dict = {"{}번".format(number+1): name for number, name in enumerate(students)}
print(std_dict)

scores = [85,92,78]
for x, y in zip(students, scores):
    print(x, y)

score_dic = {student : score for student, score in zip(students, scores)}
print(score_dic)
