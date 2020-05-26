#1.Write a Python program to sort a list of elements using the bubble sort Algorithm.
def bubble_sort(lst):
    a = len(lst)
    for i in range(a):
        for j in range(0,a-1-i,1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
l = list(map(int,input().split()))
print('list after sortting by bubble sort:')
print(bubble_sort(l))

#2.Write a Python program for sequential search (Linear search).
def linear_search(lst,a):
    for i in lst:
        if i==a:
            return True
    return False
l = list(map(int,input().split()))
n = int(input('Enter a number to search in a list:'))
a = linear_search(l,n)
if a==True:
    print('%d is present in list'%(n))
else:
    print('%d is not present in list'%(n))

#3.Write a Python program for Binary search.
def bin_search(lst,n):
    f = 0
    l = len(lst) - 1
    lst.sort()
    while f <= l:
        mid = l + (f - l) // 2
        if lst[mid]==n:
            return mid
        elif n>lst[mid]:
            f = mid + 1
        else:
            l = mid - 1
    return 0
l = list(map(int,input().split()))
n = int(input('Enter number to find:'))
a = bin_search(l,n)
if a!=0:
    print('%d found'%(n))
else:
    print('%d not found'%(n))

#4.Write a python program to concatenate two lists index-wise.
def concate_list(lst1,lst2):
    for i in range(len(lst1)):
        lst1[i] = lst1[i] + lst2[i]
    return lst1
lst1 = list(map(str,input().split()))
lst2 = list(map(str,input().split()))
print(concate_list(lst1,lst2))

#5.Iterate a given list and check if a given element already exists in a       dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {'John':47,'Peter':64,'Mahi':37,'Maria':76}
v = sampledict.values()
values_dict = []
for i in roll_number:
    for j in v:
        if i==j:
            values_dict.append(i)
print(values_dict)