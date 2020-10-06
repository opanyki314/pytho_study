class Methods:
    def imeth(self, x) : # Нормальный метод экземпляра: передается self
        print([self, x] )
    def smeth(x) : # Статический метод: экземпляр не передается
        print([х])
    def cmeth(cls, х) : # Метод класса: получает класс, а не экземпляр
        print([cis, х])

    smeth = staticmethod(smeth) # Делает smeth статическим методов (или 0: впереди)
    cmeth = classmethod(cmeth)
