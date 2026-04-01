
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def speak(self):

        print(f'{self.name} says {self.sound}')

class Dog(Animal):
    def __init__(self,name,sound,breed):
        super().__init__(name,sound)
        self.breed = breed

    def fetch(self):
        print(f'{self.name} fetches the ball')

    def speak(self):
        print(f'Dog says {self.sound}')

class Cat(Animal):
    def __init__(self, name,sound, indoor):
        super().__init__(name,sound)
        self.indoor = indoor

    def speak(self):
        print(f'Cat says {self.sound}')

    def fetch(self):
        print(f'{self.name} purrs....')


dog1 = Dog('Bobby','woof','Hushpuppy')
cat1 = Cat('Hoppie','meow',True)

dog1.fetch()
cat1.fetch()

dog1.speak()
cat1.speak()