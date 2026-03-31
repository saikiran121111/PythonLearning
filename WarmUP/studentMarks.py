from functools import reduce


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def average(self):

        totalmarks = reduce(lambda acc, num: acc + num, self.marks)
        totalaverage = totalmarks / len(self.marks)

        print(f'Average of {self.name} is {totalaverage}')

        return totalaverage

    def result(self):

        if self.average() >= 50 :
            print(f'{self.name} passed')
        else :
            print(f'{self.name} failed')

    def highest(self):

        highest = reduce( lambda acc , num : acc if acc > num else num , self.marks)
        print(f'{self.name} highest mark is {highest}')


student1 = Student('Aditya',[98,95,92,90,70,60])

student1.average()

student1.result()

student1.highest()

student2 = Student('Ravi',[1,5,3,4,3,2])

student2.average()

student2.result()

student2.highest()