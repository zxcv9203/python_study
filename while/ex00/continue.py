# 주어진 if-else문에서 else문을 제거하고 if문과 continue를 사용하기
numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a, b, a/b))