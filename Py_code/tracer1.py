class tracer:
    def __init__(self, func):   # Запоминает исходный начальный счетчик
        self.calls = 0
        self.func = func
    def __call__(self, *args) : # При последующих вызовах: добавляет логику,
                                # запускает оригинал
        self.calls += 1
        print ('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)
@tracer                     # To же самое, что и spam = tracer (spam)
def spam(a, b, с) :        # Помещает spam внутрь объекта декоратора
    return a + b + с
    
print(spam(1, 2, 3))        # На самом деле обращается к объекту-оболочке tracer
print(spam('а', 'b', 'с'))  # Вызывается метод__call__ из класса
