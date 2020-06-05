#Write a program to count how many reference variables in a program.
import sys
class Count:
    pass
c = Count()
c1 = c
c2 = c1
print('Number of reference variable:',sys.getrefcount(c))


#write any program to achieve composition in Python.
class Computer:
    def __init__(self, processor, ram, motherboard):
        self.processor = processor
        self.ram = ram
        self.motherboard = motherboard

    def specification(self):
        print('Name of processor used:',self.processor)
        print('Size of RAM:{}GB'.format(self.ram))
        print('Name of motherboard:',self.motherboard)

class Customer:
    def __init__(self, name, place, pc):
        self.name = name
        self.place = place
        self.Computer = pc

    def custinfo(self):
        print('Name of customer:',self.name)
        print('Location of customer:',self.place)
        print('\nSpecification of his computer he purchased:')
        self.Computer.specification()

p = input('Enter the name of processor:')
r = int(input('Enter the size of ram:'))
m = input('Enter the motherboard name required:')

C = Computer(p,r,m)

name = input('Enter customer name:')
place = input('Enter where he live:')

cus = Customer(name, place, C)

cus.custinfo()