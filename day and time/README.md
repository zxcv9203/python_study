# [module] datetime 

## [class] datetime
```python
from datetime import datetime

# 현재 시간 표시
datetime.now()

# replace(), 값 변경
start_time = datetime.now()
start_time.replace(year=2017, month=3, day=17)

# 년월일시 입력하기
start_time = datetime(2016,11, 27)

# datetime 클래스는 빼기 연산을 지원함
start_time = datetime(2022, 11, 27)
how_long = start_time - datetime.now()
type(how_long) #  <class 'datetime.timedelta'>
how_long.days # 날짜
how_long.seconds # 시간과 분을 알려주지 x, 초로 계산

print("{}개월 {}일 남았습니다.".format(how_long.days//12, (how_long.days%)) 
```


## [class] timedelta 
시간의 연산을 가능하게 해주는 클래스
```python
import datetime
# 100일 뒤를 계산
hundred = datetime.timedelta(days = 100)
print(datetime.datetime.now + hundred)

# datetime 클래스와 timedelta 클래스끼리는 연산가능

#100일 전 계산
print(datetime.datetime.now() - hundred)

hundred_before = datetime.timedelta(days = -100)
print(datetime.datetime.now() + hundred_before

```
