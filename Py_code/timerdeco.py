import time
def timer (label = '', trace = True):
    def onDecorator(func):
        def onCall(*args, **kargs):
            start = time.time()
            result = func(*args, **kargs)
            elapsed = time.time() - start
            onCall.alltime += elapsed
            if trace:
                form = '%s %s: %.5f, %.5f'
                values = (label,func.__name__,elapsed,onCall.alltime)
                print(form % values)
            return result
        onCall.alltime = 0
        return onCall
            
    return onDecorator

