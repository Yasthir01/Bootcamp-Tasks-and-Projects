"""Manipulating strings"""


my_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

# replace '!' with a blank space
new_string = my_string.replace('!', ' ')
print(new_string)

# convert the new string to upper case
upper_string = new_string.upper()
print(upper_string)

# reverse the string
reversed_string = upper_string[::-1]  # we can use slicing to reverse a string
print(reversed_string)

