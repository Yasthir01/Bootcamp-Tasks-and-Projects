"""Program that keeps asking user for numbers and then calculates the average of those numbers"""


# we need to keep track of the sum and number of entries to work out the average
sum_of_nums = 0  # will store total of numbers entered
counter = 0  # will count how many numbers the user enters

# create a while loop that keeps on asking for a number and breaks if -1 is entered
while True:
	user_num = int(input("Enter in a number: "))
	if user_num == -1:
		break
	sum_of_nums += user_num
	counter += 1

# calculate the average
average = sum_of_nums / counter  
print(f"The average of the numbers entered is: {average}")
