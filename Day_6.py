#1.Python program to Swap Keys and Values in Dictionary.
d = dict()
for i in range(1,4):
    d[i] = input()
print(d)
d = dict(zip(d.values(),d.keys()))
print(d)

#2.Write program to implement Selection sort.
def selection_sort(lst):
    for i in range(len(lst)):
        idx = i
        for j in range(i+1,len(lst)):
            if lst[idx] > lst[j]:
                idx = j
        lst[i],lst[idx] = lst[idx],lst[i]
    return lst
l = list(map(int,input().split()))
print('Original List:',l)
print('After selection sort:')
print(selection_sort(l))

#3.Write program to implement Insertion sort.
def insertion_sort(lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i - 1
        while j>=0 and temp<lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst
l = list(map(int,input().split()))
print('Original List:',l)
print('After insertion sort:')
print(insertion_sort(l))

#4.Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list.
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
add_list = ["h", "i", "j"]
for i in add_list:
    list1[2][1][2].append(i)
print(list1)

#5.Access the value of key “history”
sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(sampleDict['class']['student']['marks']['history'])