# for 반복문

반복문은 해당하는 코드 블록을 주어진 조건만큼 반복해서 실행시키는 명령문입니다.

for 키워드를 사용하면 반복문을 사용할 수 있습니다.

for 문의 구조는 다음과 같습니다.
``` python
for value in list or tuple or strings :
	code ...
	...
```

in 키워드 뒤에 리스트나 튜플, 문자열 자료형이 올 수 있으며 for 뒤에 오는 value에 각 값들이 대입됩니다.

다음은 리스트의 요소들을 탐색하는 for문 입니다.
``` python
nums = [3, 2, 7, 4, 1]
for num in nums :
	print(num)
``` 

위의 코드를 실행시키면 `3 2 7 4 1`이 차례대로 실행되는 것을 볼 수 있습니다.

결과 값을 보면 리스트의 첫번째 값부터 마지막 값까지 순서대로 num에 대입되는 것을 알 수 있습니다.

이런식으로 반복문을 사용해서 작업을 하면 리스트의 크기를 알지 못하더라도 리스트의 끝까지 전부 탐색할 수 있습니다.

## for in range

만약 for 문을 이용해서 1 부터 1000까지 숫자를 출력하고 싶다면 어떻게 해야할까요?

``` python
nums = [1, 2, 3, ..., 1000]
```

위의 코드와 같이 1부터 1000까지의 수를 가진 리스트를 만들어서 출력하는 방법밖에 없을까요?

이런 경우 range를 이용하면 해결할 수 있습니다.

for in range 구문은 다음과 같은 형태를 가지고 있습니다.

``` python
for value in range (start, end)
```

위에서 start 부분의 숫자는 생략될 수 있으며 생략시 0으로 시작하게 됩니다.

end 부분은 end 까지가 아닌 end - 1 값까지 실행됩니다.

range 구문을 이용해서 안에 숫자를 넣으면 차례대로 1씩 증가하는 리스트를 만들게 됩니다.

예를들어

``` python
for i in range(5) : # [0, 1, 2, 3, 4]
```

위의 코드는 `range(5)`의 범위를 가지는데 이 구문은 `[0, 1, 2, 3, 4]`의 리스트를 만들게 됩니다.

다음 코드는 1부터 1000까지를 출력하는 for in range 구문입니다.

``` python
for value in range(1, 1001) :
	print(value)
```

위의 코드를 실행하면 1부터 시작해서 1000까지 실행됩니다.

## for in enumerate

만약 현재 값이 몇번째 인덱스에 들어 있는 값인지 알고 싶으면 어떻게 해야될까요?

다음 코드와 같이 range를 이용해서 출력할 수 있을 것입니다.

``` python
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)) :
	name = nums[i]
	print('{}번째 값 : {}'.format(i, name))
```

하지만 위의 방법보다 좀 더 간단하게 해결할 수 있습니다.

바로 for in enumerate 구문을 사용하면 됩니다.

for in enumerate 구문의 형태는 다음과 같습니다.

``` python
for index, value in enumerate(list) :
	code
	...
```

여기서 index는 리스트의 index를 가르키고 value 해당 리스트의 인덱스에 담긴 값을 의미합니다.

위의 for in range 구문으로 인덱스와 값을 출력한 코드를 for in enumerate로 변경하면 다음과 같습니다.

``` python
nums = [1, 2, 3, 4, 5]
for i, num in enumerate(nums) :
	print('{}번째 값 : {}'.format(i, num))
```
