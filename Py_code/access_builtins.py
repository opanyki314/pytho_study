"""
Файл access_builtins.ру (из access2_builtins2b.ру)
Направляет некоторые встроенные операции обратно методу __getattr__
класса-посредника, так что они работают в Python З.Х аналогично прямым
вызовам по именам и стандартным классическим классам Python 2.Х.
При необходимости расширьте, чтобы включить другие
имена методов __X__, используемые внутренними объектами.
"""
class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)
    def __add__(self, other):
        return self.reroute('__add__ ', other)
    def __str__(self):
        return self.reroute('__str__ ')
    def __getitem__ (self, index):
        return self.reroute('__getitem__', index)
    def __call__ (self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)
