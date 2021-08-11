"""A program that reads in names and date of birth from text file"""


f = open('DOB.txt', 'r')  # open the file in read mode
content = f.readlines()

print("Name: ")  # we only want the names for now
index = 1  # this will keep track of the names in numeric order
for i in content:
	new_content = i.split()  # split it into a list so we can access the indices
	names = new_content[0:2]  # we only want to first 2 elements which are the names
	print(' ', index,'.', *names)  # *names unpacks the values on the same line
	index += 1  # we need to increase the number after every name

print("\nBirth date: ")
j_index = 1  # this will keep track of the dates in numeric order
for j in content:
	j_content = j.split()  # split it into a list so we can access the indices
	dates = j_content[2:]  # we only want the last elements after the names
	print(' ', j_index, '.', *dates)  # *dates unpacks the values on the same line
	j_index += 1  # we need to increase the number after every date

f.close()