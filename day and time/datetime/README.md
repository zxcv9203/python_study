### 1. 현재 시간을 표시하시오
```python
from datetime import datetime 
datetime.now()
```

### 2. 2016년 1월 11일을 변수 birthday에 설정하시오
```
birthday = datetime(2016, 1, 11)
```


### 3. 2016년 1월 27일은 오늘로부터 _년 _일 입니다. 를 빈칸을 채워 출력하여라.
```
start_time = datetime(2016, 1, 27)
how_long = datetime.now() - start_time
print("2016년 1월 27일은 오늘로부터 {}년 {}일 입니다.".format(how_long.days//365, 
how_long.days%365))
```
