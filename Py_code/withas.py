class TraceBlock:
    def message(self, arg) :
        print('running ' + arg) # выполнение
    def __enter__ (self) :
        print('starting with block') # начало блока
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print ('exited normally\n') # нормальный выход
        else:
            print ('raise an exception! ' + str (exc_type) ) # генерация исключения
        return False # Распространение
if __name__ == '__main__' :
    with TraceBlock () as action:
        action.message('test 1')
        print('reached') # достигнуто
    with TraceBlock () as action:
        action.message('test 2')
        raise TypeError
        print('not reached')
