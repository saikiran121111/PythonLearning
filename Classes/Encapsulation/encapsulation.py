from multiprocessing.spawn import prepare


#1 WarmUp
class Student:
    def __init__(self,name,grade):

        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,grades):

        if isinstance(grades,int) and 0 < grades <= 100:
            self.__grade = grades

        else:
            raise ValueError(f'{grades} is not a valid grade')

    def show(self):
        print(f'{self.name} - Grade: {self.grade}')

student1 = Student('Sai',90)

student1.show()

#2 Easy

class Rectangle:
    def __init__(self,width,height):

        self.width = width
        self.height = height


    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if isinstance(width, int) and width > 0:
            self.__width = width
        else:
            raise ValueError(f'{width} is not valid')

    @height.setter
    def height(self,height):
        if isinstance(height,int) and height > 0:
            self.__height = height
        else:
            raise ValueError(f'{height} is not valid')

    @property # computed property used only to get data no hardcoded values
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2*(self.width + self.height)


rect = Rectangle(5,10)

print(rect.area)
print(rect.perimeter)


#3 Medium

class Employee:

    def __init__(self,name,salary,department):

        self.name = name
        self.salary = salary
        self.department = department

    @property
    def salary(self):
        return self.__salary

    @property
    def department(self):
        return self.__department

    @salary.setter
    def salary(self,salary):
        if isinstance(salary,int) and salary > 0:
            self.__salary = salary
        else:
            print('Salary must be greater than 0!')

    @department.setter
    def department(self,dept):
        if len(dept) == 0:
            print('Invalid Dept')
        else:
            self.__department = dept

    def give_raise(self,percent):

        if isinstance(percent,int) and 1 <= percent <= 50:
            raising = self.salary * (percent/100)
            self.salary = int(self.salary + raising)
            print(f'salary becomes {self.salary}')
        else:
            print('Raise must be between 1% and 50%')

    def transfer(self,dept):
        validate_list = ['HR','IT','Finance','Marketing']

        if dept in validate_list :
            print('Valid department')
            self.department = dept
        else:
            print('Invalid department!')


emp = Employee('Sai',50000,'IT')

emp.give_raise(200)
emp.transfer('HR')
emp.transfer('Gaming')
emp.salary = -1000