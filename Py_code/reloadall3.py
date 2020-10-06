"""
reloadall3.ру: транзитивная перезагрузка вложенных модулей (явный стек)
"""
import types
from imp import reload # from требуется в Python З.Х
from reloadall import status, tryreload, tester
def transitive_reload(modules, visited):
    while modules:
        next = modules.pop () # Удалить элемент next в конце
        status (next) # Перезагрузить это, затолкнуть атрибуты в стек
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
            if type(x) == types.ModuleType and x not in visited)
def reload_all (*modules) :
    transitive_reload(list(modules), set())
if __name__ == '__main__' :
    tester(reload_all, 'reloadall3') # Тест: перезагрузка самого себя?
