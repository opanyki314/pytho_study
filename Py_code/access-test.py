"""
Файл: access-test.ру
Код тестов: в отдельном файле, чтобы сделать возможным многократное
использование декоратора.
"""
import sys
from access2 import Private, Public

print ( '--------------------------------------------------------------------------------')
# Тест 1: имена открыты, если не объявлены закрытыми
@Private('age')             # Person = Private('age') (Person)
class Person:               # Person = onInstance с состоянием
    def __init__(self, name, age):
        self.name = name
        self.age = age      # Внутренние операции доступа
                            # выполняются нормально
    def __add__(self, N) :
        self.age += N       # Встроенные операции перехватываются
                            # подмешиваемым классом в Python З.Х
    def __str__(self) :
        return '%s: %s' % (self.name, self.age)
    
X = Person('Bob', 40)
print(X.name) # Внешние операции доступа проверяются
X.name = 'Sue'
print(X.name)
print(X)
X + 10
print(X)
try: t = X.age      # ТЕРПИТ НЕУДАЧУ, если только
                    # не используется python -О
except: print(sys.exc_info()[1])
try: X.age = 999 # To же самое
except: print(sys.exc_infо()[1])
print ('-----------------------------------------------------------------------------' )


# Тест 2: имена закрыты, если не объявлены открытыми
# Операции должны быть не Private или Public, если используются в BuiltinMixin
@Public('name', '__add__', '__str__', 'coerce__')
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def __add__(self, N):
        self.age += N
    def __str__(self) :
        return '%s: %s' % (self.name, self.age)
    
X = Person('bob', 40)
print(X.name)
X. name = 'sue'
print(X.name)
X + 10
print(X)
try: t = X.age
except: print(sys.exc_info()[1])
try: X.age = 999
except: print(sys.exc_info()[1])
