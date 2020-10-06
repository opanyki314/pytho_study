def rangetest(*argchecks):  # Проверка вхождения в диапазон
                            # позиционных аргументов
    def onDecorator(func):
        if not __debug__ :  # True, если python -0 main.py аргументы. . .
            return func     # Ничего не делать: вызвать исходную функцию напрямую
        else:               # Иначе определить оболочку на период отладки
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                                                            # Аргумент не в диапазоне
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator
