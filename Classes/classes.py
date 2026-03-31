class Cat: # A class 

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def purr(self):
        print(f'Cat named {self.name} is {self.age} years old')

cat1 = Cat('Meow',12)
cat1.purr()
