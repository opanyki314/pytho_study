def factory(aClass, *pargs, **kargs):
    return aClass(*pargs,**kargs)

class Hlam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job = None):
        self.name = name
        self.job=job



obj1 = factory(Hlam)
obj2 = factory(Person, 'Arthur', 'King')
obj3 = factory(Person, name = 'Brian')
