class Person:
    def __init__(self, name):
        self._name=name
    def getName(self):
        print('Fetch...')
        return self._name
    def setName(self, val):
        print('Change...')
        self._name = val
    def delName(self):
        print('Remove...')
        del self._name
    name = property(getName, setName, delName, 'name prperty docs')

bob = Person('Bob Poulson')
print(bob.name)
bob.name = 'Robert Poulson'
print(bob.name)
del bob.name

print('-'*30)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)
