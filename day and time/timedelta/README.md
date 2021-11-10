# 1. 오늘로부터 100일 뒤의 날짜를 출력하라.
```python
import datetime
print(datetime.datetime.now() + datetime.timedelta(day = 100))
```

# 2. hundred_after가 지금으로부터 100일 후, 9시 정각을 값으로 가지는 변수로 만드시오 (단, 정각의 기준은 초 단위까지만 맞으면 됩니다.)
```python
import datetime
hundred_after = datetime.datetime.now().replace(hour=9, minute=0, second=0) + datetime.timedelta(days= 100)
```
