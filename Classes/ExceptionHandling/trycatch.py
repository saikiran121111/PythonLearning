#1
from cmath import sqrt


def safe_divide(a,b):
    try:
        divide = a/b
    except ZeroDivisionError :
        print('Its a zero division error')

    except ValueError:
        print('Should be interger')

    else:
        print(divide)
    finally:
        print('Operation complete')


safe_divide(4,2)

#2
def get_element(lst,index):
    try:
        value = lst[index]
    except IndexError:
        print('Index is out of the bound')

    else:
        print(f'The value is {value}')
    finally:
        print('Code is excuted')

get_element([1,2,3],3)

#3
def convert_to_int(value):
    try:
        value = int(value)
    except ValueError:
        print('Cannot convert to int')
    else:
        print(value)
convert_to_int('45')

#4

def get_key(dictionary,key):
    try:
        value = dictionary[key]
    except KeyError:
        print('Key not found')
    else:
        print(value)

get_key({'Hi':25,'jai':34,'kay':33},'Hi')


#5

class NegativeNumberError(Exception):
    pass

def custom_error(value):

    try:
        if value < 0 :
            raise NegativeNumberError(f'This is a negative value')
    except NegativeNumberError :
        print(f'This is a negative value')
    else:
        return value ** 0.5

print(custom_error(-2))

#6

class FailException(Exception):
    pass

class Student:

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,grade):
        try:
            if grade < 0 or grade > 100:
                raise ValueError('Value is beyond the grading system')
            elif grade < 50:
                raise FailException('You are failed')

        except ValueError as e:
            print(e)
        except FailException as e:
            print(e)

        else:
            self.__grade = grade
            print(self.__grade)

student = Student('Ruku',-1)
