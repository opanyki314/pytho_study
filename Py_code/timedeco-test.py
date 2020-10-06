from __future__ import print_function # Python 2.X
from timerdeco import timer
import sys
force = list if sys.version_info[0] == 3 else (lambda X: X)
print ('--------------------------------------------------------------------------------' )
# Тестирование на функциях
@timer (trace=True, label='[CCC]==>')
def listcomp(N) : # Подобно listcomp = timer (. ..) (listcomp)
    return [x * 2 for x in range (N) ] # listcomp (...) запускает onCall
       
@timer ( '[МММ]==>' )
def mapcall(N):
    return force (map ( (lambda x: x * 2) , range (N) ) )   #list() для представ-
                                                            # лений Python З.Х
for func in (listcomp, mapcall) :
    result = func (5)   # Время для этого вызова, всех
                        # вызовов и возвращаемое значение
func(5000000)
print(result)
print ('allTime = %s\n' % func.alltime) # Суммарное время для всех вызовов
print ('--------------------------------------------------------------------------------' )
# Тестирование на методах
class Person:
    def __init__(self, name, pay) :
        self.name = name
        self.pay = pay
    @timer ()
    def giveRaise(self, percent):   # giveRaise = timer () (giveRaise)
        self.pay *= (1.0 + percent) # Декоратор запоминает giveRaise
    @timer (label= '**')
    def lastName(self):
        return self.name.split()[-1]    # alltime для каждого классаf
                                        # не для экземпляра
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20) # Запускает onCall (sue, .10)
print(int(bob.pay), int(sue.pay))
print(bob.lastName (), sue.lastName())  # Запускает onCall (bob),
                                        # запоминает lastName
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))
