#Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
import re
str = input('Enter the string:')
take_num_from_str = [int(i) for i in re.findall(r'\b\d+\b',str)]
sum = 0
for i in take_num_from_str:
    sum += i
print('Sum=',sum)
print('Percentage=',sum/len(take_num_from_str))