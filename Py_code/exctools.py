def safe(func, *pargs, **kargs):
    import sys
    import traceback
    try:
        func(*pargs, **args)
    except:
        traceback.print_exc()
        print(sys.exc_info()[0], sys.exc_info()[1])

import ok

safe(ok.oops)
