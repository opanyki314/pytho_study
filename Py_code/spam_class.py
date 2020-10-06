class Spam:
    numinstances =0 # Отслеживание переданного класса
    def __init__(self):
        Spam.numinstances += 1
    def printNumlnstances(cls):
        print("Number of instances: %s %s" % (cls.numinstances, cls))
    printNumlnstances = classmethod(printNumlnstances)
    
class Sub(Spam):
    def printNumlnstances(cls): # Переопределение метода класса
        print ("Extra stuff...", cls) # С вызовом первоначального метода
        Spam.printNumlnstances()
    printNumlnstances = classmethod(printNumlnstances)
               
class Other (Spam) : pass
