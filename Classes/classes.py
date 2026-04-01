class Vehicle: # A class

    def __init__(self, model, age):

        self.model = model
        self.age = age

    def ages(self):
        print(f'Vehicle named {self.model} is {self.age} years old')

car = Vehicle('Toyota',12)
car.ages()


#Inheritance

class Airplane(Vehicle):

    def __init__(self,model,age,faa_id): # should have the parent class attributes here aswell
        super().__init__(model,age) # Used to inherit the attributes from parent class
        self.faa_id = faa_id # New Attribute

    def ages(self): # overrides the parent method called method overriding
        print(f'Aeroplane named {self.model} is {self.age} years old')

class Truck(Vehicle):

    def ages(self):
        print(f'Truck named {self.model} is {self.age} years old')

class GolfCart(Vehicle):
    pass


aeroplane = Airplane('Boeing',5,1244)
truck = Truck('Ashok',30)
golfcart = GolfCart('suzuki',2)

aeroplane.ages()
truck.ages()
golfcart.ages()
