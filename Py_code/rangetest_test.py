from __future__ import print_function   # Python 2.X
from rangetest import rangetest
@rangetest(age=(0, 120)) # persinfо = rangetest (...) (persinfо)
def persinfo(name, age):
    print ('%s is %s years old' % (name, age))
    
@rangetest (M=(1, 12) , D=(1, 31), Y=(0, 2013))
def birthday(M, D, Y) :
    print('birthday = {0}/{1}/{2}'.format(M, D, Y) )
    
persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)
# persinfo('Bob', 150)
# persinfo(age=150, name='Bob')
# birthday(5, D=40, Y=1963)
# Тестирование методов с позиционными и ключевыми аргументами

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
        
    # giveRaise = rangetest (...) (giveRaise)
    @rangetest(percent=(0.0, 1.0)) # percent передается по имени или по позиции
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
bob = Person('Bob Smith', 'dev', 100000)
sue = Person('Sue Jones', 'dev', 100000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)
# bob.giveRaise(1.10)
# bob.giveRaise(percental.20)
# Тестирование опущенных аргументов co стандартными значениями
@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10) )
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)
    
omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs (1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)
# omitargs (1, 2, 3, 11)
# omitargs (1, 2, 11)
# omitargs(1, 2, 3, d«ll)
# omitargs(11, d=4)
# omitargs(d=4, a=ll)
# omitargs (1, b=ll, d«4)
# omitargs(d=8, c=7, a=ll)
# Недопустимое значение аргумента d
# Недопустимое значение аргумента с
# Недопустимое значение аргумента d
# Недопустимое значение аргумента а
# Недопустимое значение аргумента а
# Недопустимое значение аргумента b
# Недопустимое значение аргумента а
