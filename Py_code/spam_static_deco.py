class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    @staticmethod
    def printNumInstances():
        print("Number of instances: %s" % Spam.numInstances)

class Sub(Spam):
    def printNumInstances():
        print("Extra stuff...")
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)
