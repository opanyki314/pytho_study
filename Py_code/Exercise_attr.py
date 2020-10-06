class Attrs:
    def __getattr__(self, name) :
        print ('get %s' % name)
    def __setattr__(self, name, value) :
        print ('set %s %s' % (name, value))

if __name__ == '__main__':
    x = Attrs()
    x.s = 50
    x.s
    print(x.s)
    
