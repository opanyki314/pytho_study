from __future__ import print_function       # Совместимость c Python 2.Х/З.Х
class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):               # Запасной вариант для итерации
        print ('get[%s]:' % i, end='')      # Также для индексирования, нарезания
        return self.data[i]
    def __iter__(self):                     # Предпочтительнее для итерации
        print('iter=> ', end=' ')           # Допускает только один активный итератор
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):              # Предпочтительнее для операции in
        print('contains : ', end='')
        return x in self.data
        next = __next__                     # Совместимость c Python 2.Х/З.Х
if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])              # Создать экземпляр
    print(3 in X)                           # Членство
    for i in X:                             # Циклы for
        print(i, end=' | ' )
    print()
    print([i ** 2 for i in X])              # Другие итерационные контексты
    print(list(map(bin, X)))
    I = iter(X)                             # Итерация вручную
                                            # (то, что делают другие контексты)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
