class MyList:
    l = []
    def __init__(self, ml = []):
        if type(ml) == type([]): self.l = ml[:]
        if type(ml) == type(self): self.l = ml.l[:]        
    def __add__(self, val):        
        if type(val) == type([]): res = MyList();res.l = self.l + val; return res            
        if type(val) == type(self): res = MyList();res.l = self.l + val.l; return res        
    def __radd__(self, val): return self + val
    def __getitem__(self, key): return self.l[key]
    def __iter__(self): return iter(self.l)
    def __repr__(self): return 'My list is:' + repr(self.l)
    def __call__(self,val): self.l = val.l#;return val
    def append(self, val): return self.l.append(val)
    def sort(self): return sorted(self.l)

class MyListSub(MyList):
    number = 0
    def __init__(self):
        self.num = 0
        MyList.__init__(self)
    def __add__(self, val):
        self.num += 1
        MyListSub.number += 1
        print('Number of using is %s' % self.num)    
        return MyList.__add__(self, val)
    def stdout(self):
        print('Number of using is %s' % self.num)

if __name__ == '__main__':
    x=MyList()
    y=MyList()
    z=MyList()
    print(x)
    x.append(1)
    print(x)
    x.append(4)
    print(x)
    print(x + [3,4])
    print([33,14] + x)
    y.append(6)
    y.append(8)
    i = iter(y)
    print(next(i))
    print(next(i))
    print(y[1])
    print(x[1:])
    z(y)
    print(z)
    x.append(0)
    print(x)    
    print(x.sort())
    sx = MyListSub()
    sy = MyListSub()
    sy.append(81)
    print(sy + [5,4,8])
    sx.append(3)
    sx.append(8)
    sx.append(16)
    print(sx)
    print(sx + [5,4,8])
    print(sx + [6,3,5])
    sx.stdout()
    print(sx.number)
    
    
