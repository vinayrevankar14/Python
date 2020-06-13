#1.Write a program to implement Constructor with Variable Number of Arguments.
class Cons:
    def __init__(self, *args):
        print(max(args))

class Cons2:
    def __init__(self, **kwargs):
        print(kwargs)


c1 = Cons
c1(1,5,9,7,4,3,1,2,21,5,)
c2 = Cons2
c2(Monday=0,Tuesday=1,Wednesday=2,Thursday=3,Friday=4,Saturday=5,Sunday=6)

#2.Write a program to implement Constructor Overloading.
class Dem:
    def __init__(self, name, rollno, place):
        self.name = name
        self.rollno = rollno
        self.place = place

class Deme:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        Dem.__init__(self)
d = Deme('Vinay',23,'Thane')
print(d.name)

#3.Write a program to implement multiple inheritance.
class Customer:
    def __init__(self):
        self.name = input('Enter name:')
        self.id = int(input('Enter customer id:'))

class Car:
    def __init__(self):
        self.company = input('Car company name:')
        self.model = input('Model name:')

class Carinfo(Customer,Car):
    def __init__(self):
        Customer.__init__(self)
        Car.__init__(self)

    def carordinfo(self):
        print('\nName of Customer:',self.name,'\nPurchase ID:',self.id)
        print('\nCar ordered info:')
        print('\nCompany name:',self.company,'\nModel name:',self.model)

c = Carinfo()
c.carordinfo()

#4.Write a program to implement operator overloading in python.
class Oper:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

a = Oper(100)
b = Oper(100)
print('Addition of two Numbers : ', a + b)

#5.Write a Python program to square and cube every number in a given list of integers using Lambda.
lst = list(map(int,input().split()))
print('Original list:',lst)
square_list = [(lambda x:pow(x,2))(x) for x in lst]
print('Square of a list:')
print(square_list)
cube_list = [(lambda x:pow(x,3))(x) for x in lst]
print('Cube of a list:')
print(cube_list)