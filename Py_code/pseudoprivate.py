class C1:
    def methl(self): self.__X = 88      # Теперь я имею свой атрибут X
    def meth2(self): print(self.__X)    # Становится _С1__X в I
class C2:
    def metha(self): self.__X = 99      # Я тоже
    def methb(self): print(self.__X)    # Становится _С2__X в I
class C3(C1, C2): pass
I = C3()                                # В I есть два имени X
I.methl(); I.metha()
print(I.__dict__)
I.meth2(); I.methb()
