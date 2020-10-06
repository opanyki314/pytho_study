def Tracer (aClass) : # При декорировании @
    class Wrapper:
        def __init__ (self, *args, **kargs): # При создании экземпляров
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)   # Использование имени из
                                                    # объемлющей области видимости
        def __getattr__ (self, attrname):
            print ('Trace: ' + attrname) # Перехват всех атрибутов кроме собственных
            self.fetches += 1
            return getattr(self.wrapped, attrname)  # Делегирование
                                                    # внутреннему объекту
    return Wrapper

if __name__ == '__main__' :
    
    @Tracer
    class Spam: # Spam = Tracer (Spam)
        def display (self) : # Spam повторно привязывается к Wrapper
            print('Spam! ' * 8)
            
    @Tracer
    class Person:
        def __init__(self, name, hours, rate): # Wrapper запоминает Person
            self.name = name
            self.hours = hours
            self.rate = rate
        def pay(self):
            return self.hours * self.rate

    food = Spam ()
    food.display()
    print([food.fetches])
    bob = Person('Bob', 40, 50)
    print(bob.name)
    print(bob.pay())
    print ('')
    sue = Person('Sue', rate=100, hours=60) 
    print(sue.name)
    print(sue.pay())
    print(bob.name)
    print(bob.pay())
    print([bob.fetches, sue.fetches])
