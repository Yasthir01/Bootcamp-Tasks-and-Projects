# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = 'Lion'  # NameError. Runtime Error. Needs to be string
animal_type = "cub"  # IndentationError. Compilation Error
number_of_teeth = 16

# Below has a Logical Error. It is missing an f-string and the order of the variables are incorrect
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

print(full_spec)  # SyntaxError. Compilation Error. Missing parentheses

