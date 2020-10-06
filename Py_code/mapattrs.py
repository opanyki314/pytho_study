"""
Файл mapattrs.py (Python З.Х + 2.Х)
Главный инструмент: mapattrs () отображает все собственные
и унаследованные атрибуты экземпляра на экземпляр или класс,
из которого они унаследованы.
Предполагает, что dir() выдает все атрибуты экземпляра.
Для эмуляции наследования использует либо кортеж MRO класса,
который дает порядок поиска для классов нового стиля
(и всех классов в Python З.Х), либо рекурсивный обход для
выведения порядка DFLR классических классов в Python 2.Х.
Также здесь: inheritance() дает нейтральный к версии порядок следования
классов;
различные словарные инструменты, использующие включения Python З.Х/2.7.
"""

import pprint
def trace(X, label='', end='\n'):
    print(label + pprint.pformat(X) + end) # Симпатичный вывод
def filterdictvals(D, V):
    """
    Словарь D с элементами после удаления значения V.
    filterdictvals(dict(a=l, b=2, c=l), 1) => {'b’: 2}
    """
    return {K: V2 for (K, V2) in D.items () if V2 != V}
def invertdict(D):
    """
    Словарь D co значениями, измененными на ключи (сгруппированными по значениям).
    Все значения должны быть хешируемыми, чтобы работать
    как ключи словаря/множества.
    invertdict(dict(а=1, b=2, с=1)) => {1: ['а’, 'с'], 2: ['Ь'])
    """
    def keysof(V):
        return sorted (K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values ()) }
def dflr(cis) :
    """
    Классический порядок сначала в глубину, затем слева направо
    в дереве классов cis.
    Циклы невозможны: Python запрещает изменения в __bases__.
    """
    here = [cis]
    for sup in cis.__bases__:
        here += dflr(sup)
    return here
def inheritance(instance):
    """
    Порядок поиска при наследовании: нового стиля (MRO) или классический (DFLR)
    """
    if hasattr (instance.__class__ , '__ mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)
def mapattrs(instance, withobject=False, bysource=False):
    """
    Словарь с ключами, дающими все унаследованные атрибуты экземпляра,
    и значениями, содержащими объекты, от которых унаследован каждый атрибут,
    withobject: Еа1зе=удалить встроенные атрибуты класса object.
    bysource: Тгие=сгруппировать результат по объектам, а не атрибутам.
    Поддерживает классы со слотами, которые препятствуют наличию __dict__
    в экземплярах.
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance) :
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__ : # Слоты
                attr2obj[attr] = obj
                break
    if not withobject:
        attr2obj = filterdictvals(attr2obj , object)
    return attr2obj if not bysource else invertdict(attr2obj)

if __name__ == '__main__' :
    print('Classic classes in 2.X, new-style in З.Х')   # Классические классы
                                                        # в Python 2.X,
    # классы нового стиля в Python З.Х
    class A: attrl = 1
    class В(A): attr2 = 2
    class С(A): attrl = 3
    class D(В, С): pass
    I = D()
    print('Py=>%s' % I.attrl) # Совпадает ли поиск Python с нашим?
    trace(inheritance(I), 'INH\n') # [Порядок наследования]
    trace(mapattrs(I), 'ATTRS\n') # Атрибуты => Источник
    trace(mapattrs(I, bysource=True), 'OBJS\n') # Источник => [Атрибуты]
    print ( 'New-style classes in 2 .X and 3 .X' ) # Классы нового стиля в 2.Х и З.Х
    class A(object) : attrl = 1 # В Python З.Х указывать
                                # (object) необязательно
    class В(A): attr2 = 2
    class С(A): attrl = 3
    class D(В, С): pass
    I = D()
    print('Py=>%s' % I.attrl)
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')
