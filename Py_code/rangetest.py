trace = True
def rangetest(**argchecks):     # Проверять вхождение в диапазон для аргументов
                                # обоих видов и аргументов со стандартными значениями
    def onDecorator(func):
        if not __debug__ :  
            return func     
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            def onCall(*pargs, **kargs):
                # Все элементы pargs соответствуют первым N
                # ожидаемых аргументов по позициям
                # Остальные должны быть в kargs или быть опущены
                # из-за наличия стандартных значений
                expected = list (allargs)
                positionals = expected[:len(pargs) ]
                #print(positionals)
                for (argname, (low, high)) in argchecks.items():
                                        # Для всех аргументов, подлежащих проверке
                    if argname in kargs:
                                        # Был передан по имени
                        if kargs [argname] < low or kargs [argname] > high:
                                        # Аргумент не находится в диапазоне
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                        if kargs[argname]
                    elif argname in positionals:
                                        # Был передан по позиции
                        position = positionals.index(argname)
                        if pargs [position] < low or pargs [position] > high:
                                        # Аргумент не находится в диапазоне
                            errmsg = '{ 0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                                        # Предполагается, что не был передан: имеет стандартное значение
                        if trace:
                                        # Аргумент имеет стандартное значение
                            print('Argument "{0}" defaulted'.format(argname))
                            
                return func(*pargs, **kargs)
            return onCall
    return onDecorator
