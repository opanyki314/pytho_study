class General(Exception): pass
class Specificl(General): pass
class Specific2(General): pass
def raiser0 () : raise General () 
def raiserl(): raise Specificl() 
def raiser2(): raise Specific2()
for func in (raiser0, raiserl, raiser2) :
    try:
        func()
    except General as X: 
        print('caught: %s' % X.__class__)
