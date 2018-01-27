# 스태틱 메소드 이용 예시 1
class Person(object):
    my_class_var = 'sanghee'

    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return f'{self.year}년 {self.month}월 {self.day}일 {self.sex}입니다.'

    @classmethod
    def ssn_constructor(cls, ssn):
        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[:2]
        else:
            year = '20' + front[:2]

        if (int(sex) % 2) == 0:
            sex = '여성'
        else:
            sex = '남성'

        month = front[2:4]
        day = front[4:6]

        return cls(year, month, day, sex)

    @staticmethod
    # 클래스 네임스페이스 안에 있을 뿐 일반 함수와 차이가 없음.
    # 클래스와 연관성이 있는 함수를 클래스 안에 정의하여 클래스나 인스터스를 통해 호출하여 편하게 쓰기 위해
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


ssn_1 = '900829-1034356'
ssn_2 = '051224-4061569'

person_1 = Person.ssn_constructor(ssn_1)
print(person_1)

person_2 = Person.ssn_constructor(ssn_2)
print(person_2)

import datetime

my_date = datetime.date(2016, 10, 9)
# 클래스 통해서 스태틱 메소드 호출
print(Person.is_work_day(my_date))
# 클래스 인스턴스를 통해서 스태틱 메소드 호출
print(person_1.is_work_day(my_date))


# 스태틱 메소드 이용 예시 2
import random

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @staticmethod
    def electric():
        pokemons = ('피카츄', '라이츄', '붐볼')
        selected_pokemon = random.choice(pokemons)
        # __init__() 초기화 함수는 하나만 존재할 수 있기 때문에 다른 생성함수를 정적 메소드로 만들어 사용
        return Pokemon(selected_pokemon, '전기')

    @staticmethod
    def water():
        pokemons = ('꼬부기', '아쿠스타', '라프라스')
        selected_pokemon = random.choice(pokemons)
        # __init__() 초기화 함수는 하나만 존재할 수 있기 때문에 다른 생성함수를 정적 메소드로 만들어 사용
        return Pokemon(selected_pokemon, '물')


random_electric_pokemon = Pokemon.electric()
print(random_electric_pokemon.name)
print(random_electric_pokemon.type)