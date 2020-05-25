'''#1.Write a function to find max of three numbers.
def max_num(a,b,c):
    return max(a,b,c)   #inbuilt function which will find the maximum out of 3 values
n = int(input('1st no.:'))
m = int(input('2nd no.:'))
o = int(input('3rd no.:'))
print('Maximum of three numbers:%d'%(max_num(n,m,o)))

#2.Write a Python program to detect the number of local variables declared in a function.
def local_num():
    a = 1
    b = 2
print('Total number of local variable:',local_num.__code__.co_nlocals) #.co_nlocals is an inbuilt function which finds the number of local variables

#3.Write a recursive function to calculate the sum of numbers from 0 to 10
def sum_num(a):
    if a <= 1:
        return a
    else:
        return (a + sum_num(a-1)) #if a=10 ----> 10+9+8+7+6+5+4+3+2+1+0
n = int(input())    #10
print('Sum of number:%d'%(sum_num(n)))

#4.Create a function showStudent() in such a way that it should accept student id, name, and it’s college name  and if the id and college name is missing in function call it should show it as by default id is 1 and college name  is VITA.
def showStudent(name, student_id=1, college='VITA'):
    print('student_id:{} \nname:{} \ncollege:{}'.format(student_id,name,college))
id = int(input('Enter student id:'))
name = input('Enter student name:')
coll = input('Enter college name:')
showStudent(name,id,coll)
showStudent(name)
showStudent(name,id)

#5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    u = set(lst)    #set doesn't take duplicate element
    unique = sorted(list(u)) #this will sort the list as set is not ordered
    return unique
l = list(map(int,input().split()))
print('Original list:')
print(l)
print('Unique list:')
print(unique_list(l))'''

#6.	Write a program to obtain the sum of the first and last digit of this number 2 user defined functions 1st for first digit & 2nd for last digit
def first_digit(n):
    while n >= 10:
        n //= 10    #will give the 1st digit of a number
    return n
def last_digit(n):
    return n%10     #will give the last digit of a number
n = int(input('Enter a number:'))
print('Sum of first and last digit:%d'%(first_digit(n)+last_digit(n)))