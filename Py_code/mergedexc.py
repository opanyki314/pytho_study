sep = '-' * 45 + '\n'
# Исключение генерируется и перехватывается
print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run') # выполняется except
finally:
    print('finally run') # выполняется finally
print('after run') # после выполнения

# Исключения не генерируются
print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run') # выполняется except
finally:
    print('finally run') # выполняется finally
print('after run') # после выполнения

# Исключения не генерируютсяf с конструкцией else
print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run') # выполняется except
else:
    print('else run') # выполняется else
finally:
    print('finally run')
print('after run')
# выполняется finally
# после выполнения

# Исключение генерируется, но не перехватывается
print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run') # выполняется except
finally:
    print('finally run') # выполняется finally
print('after run') # после выполнения
