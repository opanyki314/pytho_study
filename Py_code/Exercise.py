class Adder:
    def __init__(self, data):
        self.data = data
    def __add__(self, y):
        self.add(self.data,y)
    def add(self, x=0, y=0):
        print("Not implemented")

class ListAdder(Adder):
    def add(self, x=[], y=[]):
        res = x + y
        print(res)
        return res

class DictAdder(Adder):
    def add(self, x={}, y={}):
        res = x
        res.update(y)
        print(res)
        return res

if __name__ == '__main__':
    x,y,z = Adder(1), ListAdder([2]), DictAdder(dict(v=3))
    x.add()
    a,b = [1,2,3],[4,5]
    c,d = dict(a=1,b=2),dict(c=3,d=4,e=5)
    y.add(a,b)
    y+[6,7]
    z.add(c,d)
    z+dict(f=6)
    
