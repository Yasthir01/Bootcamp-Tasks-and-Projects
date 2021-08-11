"""A program about fast food service"""



menu_items = ['Fries', 'Beef Burger', 'Chicken Burger', 'Nachos', 'Tortilla', 'Milkshake']

print("***MENU***")
print("Pick an item")
print("1.Fries\n2.Beef Burger\n3.Chicken Burger\n4.Nachos\n5.Tortilla\n6.Milkshake")

choice = int(input("\nType in number: "))
for i in menu_items:
	if choice == i:
		print(f"You have chosen {choice}")  # Nothing gets printed out

"""The reason why it doesn't print out is because when we are looping through the list it is
	printing out the strings, not the positions. 
	So, if we are going to compare a string and an integer then it wont reach the print statement"""

