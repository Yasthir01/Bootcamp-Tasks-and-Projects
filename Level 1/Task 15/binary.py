"""Converting binary numbers to decimal values"""


import math


nums = input("Enter binary number: ")
# convert the input numbers into a list
nums_list = list(nums)
decimal = 0  # this is what we want to calculate

for num in range(len(nums_list)):
	# pop out the elements
	element = nums_list.pop()
	# check if element is equal to 1
	if element == '1':
		decimal += math.pow(2, num)

print(f"Decimal Value: {decimal}")

