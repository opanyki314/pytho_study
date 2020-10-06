from types import FunctionType
from decotools import tracer, timer
def decorateAll(decorator) :
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items() :
            if type(attrval) is FunctionType:                   # Метод?
                    setattr(aClass,attr,decorator(attrval))
        return aClass
    return DecoDecorate
@decorateAll(tracer)
class Person:
    def __init__ (self, name, pay) :
        self.name = name
        self.pay = pay
    def giveRaise(self, percent):   # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent) # onCall запоминает giveRaise
    def lastName(self):             # lastName = tracer (lastName)
        return self.name.split()[-1]
    
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)                      # Запускается onCall(sue, .10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())   # Запускается onCall (bob) ,
                                        # запоминается lastName
