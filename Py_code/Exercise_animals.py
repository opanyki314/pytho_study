class Animal:
    def speak(self):
        print("I'm an animal!")
    def reply(self):
        self.speak()
class Mammal(Animal):
    def speak(self):
        print("I'm a mammal!")
class Cat(Mammal):
    def speak(self):
        print("I'm a cat!")
class Dog(Mammal):
    def speak(self):
        print("I'm a dog!")
class Primate(Mammal):
    def speak(self):
        print("I'm a primate!")
class Hacker(Primate):pass
    #def speak(self):
     #   print("I'm a hacker!")

if __name__ == '__main__':
    a,b,c,x,y,z = Animal(), Mammal(), Cat(), Dog(), Primate(), Hacker()
    a.reply()
    b.reply()
    c.reply()
    x.reply()
    y.reply()
    z.reply()
    
    
