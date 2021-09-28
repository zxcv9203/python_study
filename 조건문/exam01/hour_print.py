#아래 두 줄의 코드는 변수 hour에 현재 시간을 저장합니다.
#이 코드가 어떻게 동작하는지는 이후 강의에서 다룹니다.
from datetime import datetime 
hour = datetime.now().hour

#현재 시간이 12시보다 작을때만 print문을 실행하도록 이 아래줄에 if문을 추가하세요.
if hour < 12:
    print('오전입니다.')#if문을 추가한 이후 이 줄은 들여쓰기 되어야 합니다.
