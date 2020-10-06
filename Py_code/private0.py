class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):     # Вызывается для
                                                # self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self)    # Сгенерировать определяемое
                                                # пользователем исключение
        else:
            self.__dict__[attrname] = value     # Избежать зацикливания,
                                                # используя ключ словаря
class Test1(Privacy):
    privates = ['age']
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    x = Test1()
    y = Test2()
    x.name = 'Bob'      # Работает
    #y.name = ' Sue'    # Терпит неудачу
    print(x.name)

    y.age = 30          # Работает
    #x.age = 40         # Терпит неудачу
    print(y.age)
