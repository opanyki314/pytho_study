class General(Exception): pass
class Specificl(General): pass
class Specific2(General): pass
def raiser0 () :
    X = General () # Генерирует экземпляр суперкласса
    raise X
def raiserl():
    X = Specificl() # Генерирует экземпляр подкласса
    raise X
def raiser2():
    X = Specific2() # Генерирует экземпляр другого подкласса
    raise X
for func in (raiser0, raiserl, raiser2) :
    try:
        func()
    except General: # Соответствует суперклассу General или любому его подклассу
        import sys
        print('caught: %s' % sys.exc_info()[0])
