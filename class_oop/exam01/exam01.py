class Human() :
    '''사람'''
person1 = Human()
person2 = Human()

person1.lang = '한국어'
person2.lang = 'Engilish'
person1.name = '서울시민'
person2.name = '인도인'

def speak(person):
    print("{}이 {}로 말을합니다".format(person.name, person.lang))
Human.speak = speak
person1.speak()
person2.speak()