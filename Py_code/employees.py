from __future__ import print_function
class Employee:
    def __init__ (self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "does stuff")  # делает что-то
    def __repr__ (self) :
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)
class Chef(Employee):
    def __init__ (self, name):
        Employee.__init__ (self, name, 50000)
    def work(self):
        print(self.name, "makes food")  # готовит еду
class Server(Employee):
    def __init__ (self, name):
        Employee.__init__ (self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")    # взаимодействует
                                                        # с клиентом
class PizzaRobot(Chef):
    def __init__ (self, name):
        Chef.__init__ (self, name)
    def work(self):
        print(self.name, "makes pizza") # готовит пиццу
        
if __name__ == "__main__" :
    bob = PizzaRobot ('bob' ) # Создать робота по имени bob
    print (bob) # Выполняется унаследованный метод__ repr__
    bob.work () # Выполняется действие, специфичное для типа
    bob.giveRaise (0.20) # Повысить зарплату роботу bob на 20%
    print(bob); print()
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__ )
        obj.work()
