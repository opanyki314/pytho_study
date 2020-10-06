# Экземпляры нормально наследуют метод перехвата вызовов из классов
# и их суперклассов
class SuperMetaObj:
    def __call__ (self, classname, supers, classdict):
        print('In SuperMetaObj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class
class SubMetaObj(SuperMetaObj):
    def __New__(self, classname, supers, classdict):
        print('In SubMetaObj.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)
    def __Init__ (self, Class, classname, supers, classdict):
        print('In SubMetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
class Eggs:
    pass
print('making class')
class Spam (Eggs, metaclass=SubMetaObj()):  # Обращается к экземпляру Sub
                                            # через Super.__call
    data = 1
    def meth(self, arg):
        return self.data + arg
print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
