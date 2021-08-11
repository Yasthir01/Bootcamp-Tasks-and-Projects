"""Working with lists, dictionaries and functions"""


def total_stock_cafe(menu, stock, price):
	"""Calculates the total stock worth of the cafe"""
	# multiply each stock value with the price of the item
	dict_comp = {k: price[k] * stock[k] for k in price}
	# iterate through every item in the menu to check if it is there
	for element in menu:
		if element in dict_comp.keys():
			value = dict_comp.values()
			# sum up the values from the dictionary
			total = sum(value)
	print(f"The total stock worth in the Cafe is: {total}")


# a list that contains items in the cafe
menu = ['muffin', 'scone', 'brownie', 'coffee']

# stock value for each item on the menu
stock = {
	'muffin': 20,
	'scone': 14,
	'brownie': 12,
	'coffee': 18,
}

# price for each item on the menu
price = {
	'muffin': 22,
	'scone': 18,
	'brownie': 15,
	'coffee': 25,
}


total_stock_cafe(menu, stock, price)




