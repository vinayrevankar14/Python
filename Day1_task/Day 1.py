#1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=',')

#2.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary
d = dict()
n = int(input())
for i in range(1,n+1):
    d[i] = i*i
print(d)

#3.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized
n = int(input())
l = []
for i in range(n):
    word = input()
    l.append(word.upper())
for i in l:
    print(''.join(i))

#4.Write a program to check wheather number is even or odd using if Else statement…
n = int(input())
if n%2==0:
    print('Number is Even')
else:
    print('Number is Odd')

#5.program that grants access only to kids aged between 8-12 using  if  else statement
n = int(input('Enter the age to check:'))
if 8<n<12:
    print('You are allowed...welcome!!')
else:
    print('Sorry not allowed...Bye!')