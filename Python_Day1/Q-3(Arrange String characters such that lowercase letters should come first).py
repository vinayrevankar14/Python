#Arrange String characters such that lowercase letters should come first
#Given input String of combination of the lower and upper case arrange characters in such a way that all lowercase letters should come first.
s = input('input_string=')
lower_str = []
upper_str = []
for i in s:
    if i.islower():
        lower_str.append(i)
    else:
        upper_str.append(i)
final_sorted_list = ''.join(lower_str + upper_str)
print('arranging characters giving precedence to lowercase letters')
print(final_sorted_list)