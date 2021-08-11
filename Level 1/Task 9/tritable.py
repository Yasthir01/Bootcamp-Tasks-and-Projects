"""Using nested loops to create a number pyramid"""


for i in range(1, 10):  # the numbers going straight down
	for j in range(1, i+1 ):  # its i+1 because the end is not included in the range function
		print(i * j, end="  ")  # we need space between each number instead of a new line
	print("")  # start a new line for every iteration of i

