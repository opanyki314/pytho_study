"""
Файл access2.py (Python З.Х + 2.Х)
Декораторы классов с объявлениями атрибутов Private и Public.
Управляют внешним доступом к атрибутам, хранящимся в экземпляре или
унаследованным из его классов.
Private объявляет имена атрибутов, которые нельзя извлекать или присваивать
им значения за пределами декорируемого класса, a Public объявляет все имена,
к которым можно применять упомянутые действия.
Предостережение: в Python З.Х это работает только для явно именованных
атрибутов: в классах
нового стиля методы перегрузки операций __X__, неявно запускаемые для
встроенных операций,
не вызывают ни __getattr__ , ни __ getattribute__ . Чтобы перехватывать и
делегировать выполнение
встроенных операций, необходимо добавить здесь методы __X__.
"""
from access_builtins import BuiltinsMixin # Частичный набор!

traceMe = False
def trace(*args):
    if traceMe: print (' [' + ' '.join(map(str, args)) + ' ] ')
def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance(BuiltinsMixin):
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)
                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr) :
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)
                def __setattr__ (self, attr, value):
                    trace('set', attr, value)
                    if attr == '_onInstance__wrapped' :
                        self.__dict__[attr] = value
                    elif failIf(attr) :
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator
def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))
def Public(*attributes) :
    return accessControl(failIf=(lambda attr: attr not in attributes))
