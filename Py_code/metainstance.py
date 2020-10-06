class MetaOne(type):
    def __new__(meta, classname, supers, classdict):    # Переопределение
                                                        # метода type
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        return 'toast'
class Super(metaclass=MetaOne): # Метакласс наследуется также и подклассами
    def spam (self):            # MetaOne запускается дважды для двух классов
        return 'spam'
class Sub (Super):      # Суперкласс: наследование или отношение между экземплярами
    def eggs (self):    # Классы наследуют атрибуты от суперклассов
        return 'eggs'   # Но не от метаклассов
