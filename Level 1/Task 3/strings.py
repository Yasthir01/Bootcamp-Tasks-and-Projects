"""Declaring a variable and displaying it in an altered way"""



hero = "Super Man"

"""1. insert '^' between each character.
   2. change to upper case.
   3. strip out '^' from the beginning and end of string
"""
new_hero = hero.replace("", "^").upper().strip("^")  
print(new_hero)  # display hero as it currently is

# we need to get rid of the 2 '^' that are in between SUPER and MAN
first_half = new_hero[:9]
second_half = new_hero[12:]
print(first_half + " " + second_half)