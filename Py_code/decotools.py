# Файл decotools .ру: смешанные декораторные инструменты
import time
def tracer (func) :     # Использовать функцию, а не класс с методом __ call__
    calls = 0           # Иначе self - только экземпляр декоратора
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print ('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

def timer(label='', trace=True):    # При наличии аргументов декоратора:
                                    # предохранить аргументы
    def onDecorator (func) :        # При синтаксисе предохранить
                                    # декорированную функцию
        def onCall(*args, **kargs): # При вызовах: вызвать исходную функцию
            start = time.time()     # Состоянием являются области видимости
                                    # и атрибут функции
            result = func(*args, **kargs)
            elapsed = time.time() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, % .5f'
                values = (label, func.__name__ , elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator
