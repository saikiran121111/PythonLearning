#1
import math


class Vehicle:
    def move(self):
        print('Moving...')


class Car(Vehicle):
    def move(self):
        print('Driving!')

class Boat(Vehicle):
    def move(self):
        print('Sailing!')

class Plane(Vehicle):
    def move(self):
        print('Flying!')

list1 = [Car(),Boat(),Plane()]

for vehicles in list1 :
    vehicles.move()


#2

class Circle:

    def __init__(self,raidus):
        self.radius = raidus

    def area(self):
        a = math.pi*self.radius**2
        return a

ar = Circle(2)

print(f'Area of circle {ar.area()}')

class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        a = self.length * self.width
        return a

ar = Rectangle(30,20)

print(f'Area of Rectangle {ar.area()}')


class Triangle:

    def __init__(self,breath,height):
        self.breath = breath
        self.height = height

    def area(self):
        a = 1/2*self.breath*self.height
        return a

ar = Triangle(27,23)

print(f'Area of Triangle {ar.area()}')


#3 DuckTyping

class Printer:
    def work(self):
        print('printing')
class Scanner:
    def work(self):
        print('Scanning...')
class Photocopier:
    def work(self):
        print('Copying...')

def start_machine(machine):
    machine.work()


starti_machine = Printer()

start_machine(starti_machine)


#4
#Real world

class Notification:
    def send(self,message):
        pass

class EmailNotification(Notification):
    def send(self,messages):
        print(f'Sending Email:{messages}')

class SMSNoification(Notification):
    def send(self,messages):
        print(f'Sending SMS:{messages}')

class PushNotification(Notification):
    def send(self,messages):
        print(f'Push Notification:{messages}')

sendLoop = [EmailNotification(),SMSNoification(),PushNotification()]

for notification in sendLoop:
    notification.send('Your order is confirmed!')