def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print("{}번째 index의 값을 가져올 수 없습니다.".format(index))

list1 = [1, 2, 3]
safe_pop_print(list1, 2)
safe_pop_print(list1, 5)