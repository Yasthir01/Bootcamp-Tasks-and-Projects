"""A program that sorts numbers from two files into another file"""


with open('numbers1.txt', 'r') as file1, open('numbers2.txt', 'r') as file2, open('allNumbers.txt', 'w') as file3:
	odd_nums = file1.read()  # I placed odd numbers in the first file
	even_nums = file2.read()  # I placed even numbers in the second file

	together = odd_nums + even_nums  # add the string together
	together_list = together.split()  # convert it into a list

	# we need to convert each string element to an integer
	num_list = [int(x) for x in together_list]  
	num_list.sort()  # we now sort the list of integers in ascending order

	# we now convert it back to strings so we can write to file
	string_list = [str(num) for num in num_list]  
	print(string_list)
	
	for element in string_list:
		file3.write(element)  # write each number to the 'allNumbers.txt' file
		file3.write(" ")  # allow a space to be between each number