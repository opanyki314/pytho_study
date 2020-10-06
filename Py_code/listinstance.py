class ListInstance:
    """
    Подмешиваемый класс, который предоставляет форматированную функцию
    print() или str () для экземпляров через наследование реализованного
    в нем метода __str__ ; отображает только атрибуты экземпляра; self
    является экземпляром самого нижнего класса;
    имена __X предотвращают конфликты с атрибутами клиента
    """
    def __attrnames(self):
        result = ''
        for attr in sorted (self.__dict__ ) :
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    def __str__(self) :
        return '<Instance of %s(%s), address %s:\n%s>' % (
                        self.__class__.__name__ ,       # Имя класса
                        self.__supers(),
                        id(self),                       # Адрес
                        self.__attrnames())             # Список имя=значение
    def __supers(self):
        res = []
        for sup in self.__class__.__bases__:
             res.append(sup.__name__)
        return ', '.join(res)
if __name__ == '__main__' :
    import testmixin
    testmixin.tester(ListInstance)
