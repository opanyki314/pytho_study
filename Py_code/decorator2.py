class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)

@Tracer
def spam(a,b,c):
    print(a+b+c)

@Tracer
def eggs(x,y):
    print(x ** y)
    
spam(1,2,3)
spam(a=4,c=6,b=5)

eggs(2,16)
eggs(4, y=4)
