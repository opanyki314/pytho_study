class Name:
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('Fetch...')
        return instance._name
    def __set__(self, instance, val):
        print('Change...')
        instance._name = val
    def __delete__(self, instance):
        print('Remove...')
        del instance._name
class Person:
    def __init__(self, name):
        self._name=name
    name = Name()

bob = Person('Bob Poulson')
print(bob.name)
bob.name = 'Robert Poulson'
print(bob.name)
del bob.name

print('-'*30)
sue = Person('Sue Jones')
print(sue.name)
print(Name.__doc__)
