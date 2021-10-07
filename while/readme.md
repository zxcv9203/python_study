## while 반복문
+ 조건이 참인 경우 계속 실행하는 반복문
``` python
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요')
```
+ for 반복문으로 작성한 코드는 while 반복문으로 작성할  수 있다.

## break, continue
+ break
    + 반복문을 종료시키는 기능
``` python
# 사이즈가 32인 바지의 위치를 한번만 출력하고 프로그램이 종료되도록 만들어 보세요.
sizes = [33, 35,34, 37, 32, 35, 39, 32, 35, 29]
for i, size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
        break
```

+ continue
    + 반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능
``` python
# 주어진 if-else문에서 else문을 제거하고 if문과 continue를 사용하기
numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a, b, a/b))
```