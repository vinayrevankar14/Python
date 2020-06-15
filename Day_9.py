#1.Write a function to compute divide by zero and use try/except to catch the exceptions.
def div_by_zero(a,b):
    try:
        ans = a//b
        print('Number is divided and answer:',ans)
    except ZeroDivisionError:
        print('Can\'t divide as number is divided by zero')
n = int(input('Enter the number to be divided:'))
x = int(input('Enter the number to divide:'))
div_by_zero(n,x)

#2.Write python program to check that given number is valid mobile number or not?
import re
def valid_mobileno(n):
    valid = re.compile(r'(0|\+91)?[0-9]{10}$')
    return valid.match(n)
n = input('Enter the mobile number to check valid or not:')
if (valid_mobileno(n)):
    print('valid mobile number')
else:
    print('Not valid.... please put valid mobile number')

#3.Write python program to check  that given email address is valid or not?
import re
def valid_email(s):
    valid = re.compile(r'[a-z0-9_.]+@[a-z]+\.[a-z]+')
    return valid.match(s)
e = input('Enter your email id:')
if (valid_email(e)):
    print('Given email id is valid')
else:
    print('Given email id is not valid')

#4.Write a python program to check given car registration number is valid Maharashtra state registration number or not?
import re
def car_registrationno_valid(c):
    valid = re.compile(r'^MH[-][0-9]{2}[-][A-Z+]{2}[-][0-9]{4}$')
    return valid.match(c)
p = input('Enter the car registration number:')
if (car_registrationno_valid(p)):
    print('Valid registration number')
else:
    print('Not a valid registartion number')

#5.Write a python program to decorate arithmetic operations.
def arithmetic(func):
    def operations(a,b):
        print('Multiplication of number=',a*b)
        print('Division of a number=',a/b)
        print('Remainder of number=',a%b)
        func(a, b)
    return operations
@arithmetic
def add_sub(a,b):
    print('Addition of two numbers=',a+b)
    print('Subtraction of two numbers=',a-b)

x = int(input('Enter the 1st number:'))
y = int(input('Enter the 2nd number:'))
add_sub(x,y)

#6.Write a python program to generate Fibonacci Numbers upto 100 using generator.
def fibonacci(n):
    x,y = 0,1
    for i in range(n):
        yield x
        x,y = y,x+y

n = int(input('Enter the number:'))
for i in fibonacci(n):
    if i > n:
        break
    print(i)
