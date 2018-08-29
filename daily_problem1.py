'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether ANY TWO NUMBERS from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

list_num = [10, 15, 3, 7]
target_num = 13

#create a dictionary, with key and the value is the remainder of target_num
for num in list_num:
	remainder = target_num - num
	if remainder in list_num:
		print("{} = {} + {}".format(target_num, num, remainder))
		break
	break

'''
NEXT LEVEL,
not it is not only 2 numbers, but now we could add up more than 2 numbers
'''
list_num = [10, 15, 3, 7, 5, 4, 6]
target_num = 20
lists = []
current_list = []

for i in range(len(list_num)):
	remainder = target_num - list_num[i]
	if remainder < 0:
		continue
	for j in range(i + 1, len(list_num)):
		if remainder - list_num[j] < 0:
			remainder = target_num - list_num[i]
			current_list = []
		else:
			remainder -= list_num[j]
			current_list.append(list_num[j])
			if remainder == 0:
				current_list.append(list_num[i])
				lists.append(current_list)
				current_list = []
				remainder = 0

print(lists)
		