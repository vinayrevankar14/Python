#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
def middle_str(str1,str2):
    mid_index = int(len(str1)/2)
    print('Original string-->',str1,str2)
    insert_middle = str1[:mid_index - 1] + str2 + str1[mid_index - 1:]
    print('After appending the string --->',insert_middle)
str1 = input('Enter first string:')
str2 = input('Enter second string:')
middle_str(str1,str2)