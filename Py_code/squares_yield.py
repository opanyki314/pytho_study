class Squares:
    def __init__(self, start, stop):    # Сохранить состояние при создании
        self.start = start
        self.stop = stop
    def __iter__(self) :                    # Получить объект итератора при вызове iter
        for value in range(self.start, self.stop +1):
            yield value ** 2
