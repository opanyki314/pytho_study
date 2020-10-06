"""
Регистрирует и обрабатывает сведения о людях.
Для тестирования классов из этого файла запустите его напрямую.
"""
from classtools import AttrDisplay  # Использовать обобщенный инструмент
                                    # отображения
class Person(AttrDisplay):          # Комбинирование с классом верхнего уровня
    """
    Создает и обрабатывает записи о людях
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]    # Предполагается, что фамилия указана последней
    def giveRaise(self, percent):       # Процент должен находиться между 0 и 1
        self.pay = int(self.pay*(1 + percent))

class Manager(Person):
    """
    Настроенная версия Person co специальными требованиями
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus =.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay=100000)
    print(bob)
    print(sue)

    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
