class Methods(object):
    def imeth(self, x) : # Нормальный метод экземпляра: передается self
        print([self, x] )
    @staticmethod
    def smeth(x) : # Статический метод: экземпляр не передается
        print([x])
    @classmethod
    def cmeth(cls, х) : # Метод класса: получает класс, а не экземпляр
        print([cls, х])
    @property # Свойство: значение вычисляется при извлечении
    def name(self):
        return 'Bob ' + self.__class__.__name__
    
