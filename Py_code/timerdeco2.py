import time
def timer (label = '', trace = True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__ (self, *args, **kargs):
            start = time.time()
            result = self.func(*args, **kargs)
            elapsed = time.time() - start
            self.alltime += elapsed
            if trace:
                form = '%s %s: %.5f, %.5f'
                values = (label,self.func.__name__,elapsed,self.alltime)
                print(form % values)
            return result
    return Timer

