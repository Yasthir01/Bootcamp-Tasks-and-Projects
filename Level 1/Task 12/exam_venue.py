"""A program that records ID numbers of students and writes them to a file"""


file = open("RegForm.txt", "w")
# number of students that will be registering
num_students = int(input("How many students will be registering?: "))

for student in range(1, num_students+1):
	id_num = input("Enter ID number: ")
	file.write(f"{id_num}\n")

file.close()
