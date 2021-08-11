"""A program to determine leap years"""

 
# the year that the user wants to start with
start_year = int(input("What year do you want to start with? : "))
# the number of years to check
num_years = int(input("How many years do you want to check? : "))

# if a year is a multiple of 4 then it is a leap year
for year in range(start_year, start_year + num_years):
	if year % 4 == 0:
		print(f"{year} is a leap year")
	else:
		print(f"{year} isn't a leap year")