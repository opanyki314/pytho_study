"""
Файл argtest.ру (Python З.Х + 2.Х): декоратор функций, который выполняет
произвольные переданные проверки для аргументов, передаваемых любой функции
или методу. Двумя примерами могут служить проверка на предмет вхождения
в диапазон и проверка типов; valuetest обрабатывает более произвольные
проверки для значения аргумента.
Аргументы для декоратора указываются по ключевым словам. В фактическом
вызове аргументы могут передаваться по позициям или по ключевым словам,
а аргументы со стандартными значениями разрешено опускать. Примеры
сценариев использования приведены в коде самотестирования.
Предостережение: не полностью поддерживает вложение, потому что аргументы
посредника вызовов отличаются; не проверяет дополнительные аргументы,
переданные в *args декорированного класса; может оказаться не проще,
чем assert, исключая заготовленные сценарии использования.
"""
trace = False
def rangetest(**argchecks):
    return argtest(argchecks, lambda arg, vals: arg < vals[0] or arg > vals[1])
def typetest(**argchecks):
    return argtest(argchecks, lambda arg, type: not isinstance(arg, type))
def valuetest(**argchecks):
    return argtest(argchecks, lambda arg, tester: not tester(arg))
def argtest(argchecks, failif): # Проверка аргументов согласно failif
                                # и критерия
    def onDecorator (func) :    # onCall предохраняет func, argchecks, failif
        if not __debug__ :      # Ничего не делать, если python -О main.py
                                # аргументы, . .
            return func
        else:
            code = func.__code__
            expected = list(code.co_varnames[:code.co_argcount])
            def onError(argname, criteria):
                errfmt = '%s argument "%s" not %s'
                raise TypeError(errfmt % (func.__name__, argname, criteria))
            def onCall(*pargs, **kargs):
                positionals = expected[:len(pargs)]
                for (argname, criteria) in argchecks.items() : # Для всего,
                                                                # что проверяется
                    if argname in kargs:                # Передается по имени
                        if failif(kargs[argname], criteria):
                            onError(argname, criteria)
                    elif argname in positionals:        # Передается по позиции
                        position = positionals.index(argname)
                        if failif(pargs[position], criteria):
                            onError(argname, criteria)
                    else:                               # Опущен, т.к. имеет стандартное значение
                        if trace:
                            print('Argument "%s" defaulted' % argname)
                return func(*pargs, **kargs)    # Нормально: запустить
                                                        # исходный вызов
            return onCall
    return onDecorator


if __name__ == '__main__' :
    import sys
    def fails(test) :
        try: result = test()
        except: print('[%s] ' % sys.exc_info() [1])
        else: print('?%s?' % result)

    print('-'*80)
    # Заготовленные сценарии использования: диапазоны, типы
    @rangetest(m=(1, 12), d=(1, 31), y=(1900, 2013))
    def date(m, d, y) :
        print('date = %s/%s/%s' % (m, d, y) )
    date(1, 2, 1960)
    fails(lambda: date(1, 2, 3))
    @typetest(a=int, c=float)
    def sum(a, b, c, d) :
        print (a + b + c + d)
    sum(1, 2, 3.0, 4)
    sum(1, d=4, b=2, c=3.0)
    fails(lambda: sum('spam', 2, 99, 4))
    fails(lambda: sum(1, d=4, b=2, c=99))
    print('-'*80)
    # Произвольные / смешанные проверки
    @valuetest(word1=str.islower, word2=(lambda x: x[0].isupper()))
    def msg(word1='mighty', word2='Larch', label='The'):
        print ('%s %s %s' % (label, word1, word2))
    msg() # wordl и word2 имеют стандартные значения
    msg('majestic', 'Moose')
    fails(lambda: msg('Giant', 'Redwood'))
    fails(lambda: msg('great', word2='elm'))
    print('-'*80)
    # Ручные проверки типов и вхождения в диапазон
    @valuetest (A=lambda х: isinstance (х, int), B=lambda х: х > 0 and х < 10)
    def manual (А, В) :
        print(А + В)
    manual(100, 2)
    fails(lambda: manual(1.99, 2))
    fails(lambda: manual(100, 20))
    print('-'*80)
    # Вложение: выполняются обе проверки за счет вложения посредников
    # для исходной функции.
    # Нерешенная проблема: внешние уровни не проверяют позиционные аргументы
    # из-за отличающейся сигнатуры функции посредника вызовов;
    # когда trace=True, вследствие сигнатуры посредника все аргументы X
    # кроме последнего классифицируются как имеющие стандартные значения.
    @rangetest(X=(1, 10))
    @typetest (Z=str)   # Только самый внутренний уровень
                        # проверяет позиционные аргументы
    def nester(X, Y, Z) :
        return('%s-%s-%s' % (X, Y, Z))
    print(nester(1, 2, 'spam')) # Исходная функция выполняется
                                # надлежащим образом
    fails(lambda: nester(1, 2, 3))  # Вложенный typetest
                                    # выполняется: позиционные
    fails(lambda: nester(1, 2, Z=3))    # Вложенный typetest
                                        # выполняется: ключевой
    fails(lambda: nester(0, 2, 'spam')) # <== Внешний rangetest не
                                        # выполняется: позиционные
    fails(lambda: nester(X=0, Y=2, Z='spam'))   # Внешний rangetest выполняется:
                                                # ключевые
