
class Person(object):
    my_class_var = 'sanghee'

    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return f'{self.year}년 '

    def ssn_constructor(cls, ssn):
        front, back = ssn.split('-')