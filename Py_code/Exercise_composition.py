class Lunch:
    def __init__(self):
        self.cust1 = Customer()
        self.ivan = Employee()
    def order(self, foodName):
        self.cust1.placeOrder(foodName, self.ivan)
    def result(self):
        self.cust1.printFood()
class Customer:
    def __init__(self):
        self.foodName = ''
    def placeOrder(self, foodName, employee):
        employee.takeOrder(foodName)
        self.foodName = foodName
    def printFood(self):
        print('The food is %s' % (self.foodName))
class Employee:
    def takeOrder(self, foodName):
        b1 = Food(foodName)
class Food:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    x = Lunch()
    x.order("Borsch")
    x.result()
    
