#1.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
a = list(map(int,input().split()))
b = []
print(a)
for i in a:
    b.append(i**2)  #will add square of an element in a list
print(b)

#2.From a list containing ints, strings and floats, make three lists to store them separately.
a = [1,2,3,'hello','mumbai',2.0,6.6666]
it = []
st = []
fl = []
for i in a:
    if type(i)==int:
        it.append(i)    #if element is integer in a list
    elif type(i)==str:
        st.append(i)    #if element is string in a list
    elif type(i)==float:
        fl.append(i)    #if element is float in a list
print(it)
print(st)
print(fl)

#3.	Print the pattern
n = int(input('Enter the number'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()     #cursor to the next line

#4.Accept data in two 3*3  matrix and calculate the sum of the matrices.
sum_matrix = [[0,0,0],[0,0,0],[0,0,0]]
print('Input for 1st matrix:\n')
    #input for 1st matrix
matrix_1 = [[int(input()) for j in range(3)] for i in range(3)]
print('Input for 2nd matrix:\n')
    #input for 2nd matrix
matrix_2 = [[int(input()) for j in range(3)] for i in range(3)]
    #sum of two matrix
for i in range(3):
    for j in range(3):
        sum_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]
print('1st matrix:',matrix_1)
print('2nd matrix:',matrix_2)
print('Sum of two matrix:',sum_matrix)

#5.Write a Python program to check whether a given number is a narcissistic number or not.
def narcissistic(n):
    l = len(str(n)) #convert the digit to string then find the lenght of it
    p = int(l) #typecasted to integer
    digit = [int(i) for i in str(n)]
    sum_list = [(i**p) for i in digit]
    s = sum(sum_list)
    if s==n:
        print('%d is narcissistic' %(n))
    else:
        print('%d is not narcissistic' %(n))
num = int(input('Enter the number to find it\'s narcissistic:'))
narcissistic(num)