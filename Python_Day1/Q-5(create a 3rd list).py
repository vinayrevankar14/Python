#Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second
listOne = list(map(int,input().split()))
listTwo = list(map(int,input().split()))
listthird = []

odd_index_element = listOne[1::2]
print('Element at odd-index positions from list one')
print(odd_index_element)

even_index_element = listTwo[0::2]
print('Element at even-index positions from list two')
print(even_index_element)

listthird = odd_index_element + even_index_element
print('Printing Final third list')
print(listthird)