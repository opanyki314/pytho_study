def oops():
    raise MyError

class MyError(Exception):
    def __init__(self):
        print('This my is exception')
