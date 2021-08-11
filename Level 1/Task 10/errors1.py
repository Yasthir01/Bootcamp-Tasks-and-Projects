# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program")  # SyntaxError. This is a Compilation Error. We needed to add parentheses
print ("\n")  # IndentationError and SyntaxError. This is a Compilation Error. We needed to unindent and add parentheses

# Entire block of code need to be unindented. Indentation Error. Compilation error
age_str = "24"  # NameError. Runtime Error. Needed to use '=' and not '=='
age = int(age_str)  # ValueError. Runtime Error. Needed just 24 and not whole string
print(f"I'm {age} years old")  # TypeError. Runtime Error
three = 3

answer_years = age + three  # TypeError. Runtime error. Three above cannot be string

# SyntaxError. Compilation error. Needed to add parentheses
print(f"The total number of years: {answer_years}")  # Logical Error. answer_years should be variable not string  

answer_months = (answer_years * 12) + 6  # NameError. Runtime Error. Variable should be answer_years
# There was also a Logical Error above. The program didn't add the 6 months

# SyntaxError. Compilation error. Missing parenthes
print(f"In 3 years and 6 months, I'll be {answer_months} months old")  # TypeError. Runtime Error


#HINT, 330 months is the correct answer

