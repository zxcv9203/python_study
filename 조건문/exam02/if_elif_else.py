scissor = '가위'
rock = '바위'
paper = '보'


win = '승리'
draw = '무승부'
lose = '패배'

mine = "가위"
yours = "바위"

if mine == yours:
    result = draw
else:
    if yours == rock and mine == paper:
        result = win
    elif yours == paper and mine == scissor:
        result = win
    elif yours == scissor and mine == rock:
        result = win
    else:
        result = lose

print(result)
