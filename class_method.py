# 클래스 메소드 이용 예시 1
class Employee(object):

    raise_amount = 1.1

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def full_name(self):
        return f'{self.first} {self.last}'

    def get_pay(self):
        return f'현재 {self.full_name()}의 연봉은 {self.pay}입니다.'

    @classmethod
    def change_raise_amount(cls, amount):
        while amount < 1:
            print('[경고] 인상율은 "1"보다 작을 수 없습니다.')
            amount = input('[입력] 인상율을 다시 입력해 주십시오.\n=> ')
            amount = float(amount)
        # cls를 통해 클래스 'Employee'에 접근한 뒤, 클래스 속성인 'raise_amount'에 직접 접근
        cls.raise_amount = amount
        print(f'인상율 "{amount}"가 적용 되었습니다.')


emp_1 = Employee('Sanghee', 'Lee', 50000)
emp_2 = Employee('Minjung', 'Kim', 60000)

print(emp_1.get_pay())
print(emp_2.get_pay())

Employee.change_raise_amount(1.3)

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.get_pay())
print(emp_2.get_pay())


# 클래스 메소드 이용 예시 2
class Person(object):
    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return f'{self.year}년 {self.month}월 {self.day}일 {self.sex}입니다'

    @classmethod
    # 인자/매개변수 정보형태가 표준적이지 않은 경우, 클래스 메소드를 이용해서 대체 생성자 만듦
    def ssn_constructor(cls, ssn):
        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[0:2]
        else:
            year = '20' + front[0:2]

        if (int(sex) % 2) == 0:
            sex = '여성'
        else:
            sex = '남성'

        month = front[2:4]
        day = front[4:6]

        return cls(year, month, day, sex)


person_1 = Person(1990, 8, 29, '남성')
print(person_1)

ssn_2 = '900829-1034356'
ssn_3 = '051224-4061559'

person_2 = Person.ssn_constructor(ssn_2)
print(person_2)

person_3 = Person.ssn_constructor(ssn_3)
print(person_3)