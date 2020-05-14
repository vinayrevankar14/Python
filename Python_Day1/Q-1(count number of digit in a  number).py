#Given a number count the total number of digits in a number
n = int(input('Enter the number='))
count = 0
while n>0:
    count += 1
    n = n//10
print('Number of digit in a number=',count)