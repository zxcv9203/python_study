# 사이즈가 32인 바지의 위치를 한번만 출력하고 프로그램이 종료되도록 만들어 보세요.
sizes = [33, 35,34, 37, 32, 35, 39, 32, 35, 29]
for i, size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
        break