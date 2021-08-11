"""Task about casting in Python"""


# input statements to gather favourite restaurant and favourite number
fav_rest = input("Enter in the name of your favourite restaurant: ")
int_fav = int(input("Enter in your favourite number: "))

# display the user's inputs
print(f"Your favorite restaurant is {fav_rest}")
print(f"Your favorite number is {int_fav}")




""" Trying to cast fav_rest to an int: 

int_rest = int(fav_rest)
print(int_rest)

We get an error that reads "ValueError: invalid literal for int() with base 10".

We get this error when you try to convert a string value that is not formatted as an integer.
"""
