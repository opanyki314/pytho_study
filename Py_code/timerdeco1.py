# Файл timerdecol.ру
# Предостережение: область все же отличается - список в Python 2.Х,
# итерируемый объект в Python З.Х
# Предостережение: в таком виде timer не будет работать с методами
# (см. ответ на контрольный вопрос)
import time, sys
force = list if sys.version_info[0] == 3 else (lambda X: X)
class timer:
    def __init__ (self, func):
        self.func = func
        self.alltime = 0
    def __call__ (self, *args, **kargs):
        start = time.time()
        result = self.func(*args, **kargs)
        elapsed = time.time() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result
@timer
def listcomp(N):
    return [x * 2 for x in range (N) ]
@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))
result = listcomp(5)    # Время для этого вызова, всех вызовов
                        # и возвращаемое значение
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print ('allTime = %s' % listcomp.alltime)
print ('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print ('allTime = %s' % mapcall.alltime)   # Суммарное время для всех
                                            # вызовов mapcall
print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
