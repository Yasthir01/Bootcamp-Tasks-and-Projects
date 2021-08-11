"""A program on an Investment Calculator"""

import math


# user inputs

# the amount they are depositing
P = int(input("How much are you depositing? : "))
# the interest rate
i = int(input("What is the interest rate? : "))
# the number of years of the investment
t = int(input("Enter the number of years of the investment: "))
# simple or compound interest
interest = input("Enter either 'Simple' or 'Compound' interest: ").lower()

# the 'r' variable is the interest divided by 100
r = i / 100

# check if the user entered either Simple or Compound and perform the relevant calculations

# Simple Interest Formula : A = P*(1+r*t)  N.B.  A is the total received or accumulated amount
if interest == 'simple':
	A = P * (1 + r*t)
elif interest == 'compound':
	# Compound Interest Formula : A = P* math.pow((1+r),t)
	A = P * math.pow((1 + r), t)  # t is the power

# print out the Accrued amount ie. the received or accumulated amount
print(f"The Accrued amount is : {round(A, 2)}") 



