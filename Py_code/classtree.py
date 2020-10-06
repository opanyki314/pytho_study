"""
classtree.ру: подъем по деревьям наследования с применением связей между
пространствами имен и отображением находящихся выше суперклассов с отступом
согласно высоте
"""
def classtree(cls, indent):
    print('.' * indent + cls.__name__)  # Вывести здесь имя класса
    for supercls in cls.__bases__:      # Вызвать рекурсивно для всех
                                        # суперклассов
        classtree(supercls, indent+3)   # Может посетить суперкласс
                                        # более одного раза
def instancetree(inst):
    print('Tree of %s' % inst)          # Показать экземпляр
    classtree(inst.__class__ , 3)       # Подняться к его классу
def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C) : pass
    class E: pass
    class F(D,E) : pass
    instancetree(B())
    instancetree(F())
if __name__ == '__main__': selftest ()
