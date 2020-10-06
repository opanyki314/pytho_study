traceMe = False
def trace(*args):
    if traceMe: print ('[' + ' '.join(map(str, args)) + ']')
    
def Private(*privates) : # privates в объемлющей области видимости
    def onDecorator(aClass): # aClass в объемлющей области видимости
        class onlnstance: # wrapped в атрибуте экземпляра
            def __init__ (self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__ (self, attr):   # Для собственных атрибутов
                                            # getattr не вызывается
                trace ( 'get:' , attr) # Предполагается, что остальные внутри wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)
            def __setattr__ (self, attr, value): # Операции доступа извне
                trace ('set:', attr, value) # Остальные выполняются нормально
                if attr == 'wrapped' :  # Разрешить доступ к собственным
                                        # а трибутам
                    self.__dict__[attr] = value # Избежать зацикливания
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr (self .wrapped, attr, value) # Атрибуты внутреннего объекта
        return onlnstance # Либо использовать __diet__
    return onDecorator
if __name__ == '__main__':
    traceMe = True
    @Private('data', 'size') # Doubler = Private (...) (Doubler)
    class Doubler:
        def __init__ (self, label, start):
            self.label = label # Операции доступа внутри целевого класса
            self.data= start # Не перехватываются: выполняются нормально
        def size (self):
            return len (self .data) # Методы запускаются без какой-либо проверки
        def double (self) : # Потому что защита не наследуется
            for i in range(self.size()) :
                self.data[i] = self.data[i] * 2
        def display(self) :
            print('%s => %s' % (self.label, self.data))
X = Doubler ('X is', [1, 2, 3])
Y = Doubler('Y is', [-10, -20, -30])
                # Весь следующий код выполняется успешно
print(X.label)  # Операции доступа извне целевого класса
X. display(); X.double(); X.display()   # Перехватываются: проверяются,
                                        # делегируются
print(Y.label)
Y. display(); Y.double()
Y.label = 'Spam'
Y.display()

# Весь следующий код должным образом терпит неудачу
"""
print(X.size()) # Выводится TypeError: private attribute fetch: size
print(X.data)
X.data = [1, 1, 1]
X.size = lambda S: 0
print(Y.data)
print(Y.size ())
"""
