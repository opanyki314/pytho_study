def safe(func, *pargs, **kargs):
    import sys
    try:
        func(*pargs, **args)
    except:
        print(sys.exc_info)

import oops from o1
