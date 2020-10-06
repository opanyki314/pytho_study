class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()
    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()
    
class Customer:
    def line(self):
        print("I'm a customer!")
class Clerk:
    def line(self):
        print("I'm a clerk!")
class Parrot:
    def line(self):
        print("I'm a parrot!")

if __name__ == '__main__':
    Scene().action()
    
    
