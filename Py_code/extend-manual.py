class Clientl:
    def __init__ (self, value) :
        self.value = value
    def spam(self):
        return self.value * 2
class Client2:
    value = 'ni?'
def eggsfunc(obj):
    return obj.value * 4
def hamfunc(obj, value):
    return value + 'ham'
Clientl.eggs = eggsfunc
Clientl.ham = hamfunc
Client2.eggs = eggsfunc
Client2.ham = hamfunc
X = Clientl('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))
Y = Client2 ()
print(Y.eggs())
print(Y.ham('bacon'))
