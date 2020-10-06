class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)
    
if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc') # Метод init r унаследованный от списка
    print (x) # Метод repr , унаследованный от списка
    print(x[1]) # MyList.__getitem__
    print (x[3]) # Настраивает метод из суперкласса списка
    x.append('spam'); print(x) # Атрибуты из суперкласса списка
    x.reverse(); print(x)
