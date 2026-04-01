
#1
class Animal:
    def __init__(self,name,sound):

        self.name = name
        self.sound = sound

    def speak(self):
        print(f'{self.name} says {self.sound}')

class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog = Dog('Bobby','Woof')
cat = Cat('Cutie','Meow')

dog.speak()
cat.speak()

