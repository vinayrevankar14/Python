#1.Python Program to Read a Number n And Print the Series “1+2+…..+n= “
n = int(input('Enter a number:'))
l = []
for i in range(n):
    l.append(int(input()))
for i in l:
    if i==n:
        print(i,end='')
    else:
        print(i,end='+')
print('=',sum(l))

#2.Write a Python program to count the number of even and odd numbers from a series of numbers.
l = list(map(int,input().split()))
print(l)
count_even = 0
count_odd = 0
for i in l:
    if i%2==0:
        count_even += 1
    else:
        count_odd += 1
print('Number of even number=',count_even)
print('Number of odd number=',count_odd)

#3.Write a Python program to create the multiplication table (from 1 to 10) of a number.
for i in range(1,11):
    for j in range(1,11):
        print(j,'x',i,'=',j*i,end='\t')
    print(' ')

#4.Given the triangle of consecutive odd  numbers find sum of row elements.
def row_sum(n):
    sum = n**3
    return sum
n = int(input())
print(row_sum(n))

#5.Write python program to print the pattern
n = int(input('Enter the number:'))
for i in  range(1,n+1):
    for j in range(i):
        print(i,end='')
    print()