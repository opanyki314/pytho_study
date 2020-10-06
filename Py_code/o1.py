def oops():
    raise MyError('spam')

class MyError(Exception):
    def __init__(self):
        print('This my is exception')
