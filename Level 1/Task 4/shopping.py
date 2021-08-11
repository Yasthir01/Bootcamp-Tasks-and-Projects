"""Getting the names and prices of products"""



# get the names and prices of 3 products

# first product
product_1 = input("Enter the NAME of the product: ")
price_1 = float(input("Enter the PRICE of the selected product: "))

# second product
product_2 = input("Enter the NAME of the product: ")
price_2 = float(input("Enter the PRICE of the selected product: "))


# third product
product_3 = input("Enter the NAME of the product: ")
price_3 = float(input("Enter the PRICE of the selected product: "))


# calculate total price of the products
total = price_1 + price_2 + price_3

# calculate the average price of the three products
average = total / 3


# print out a final message for the user
print(f"The Total of {product_1}, {product_2}, {product_3} is R{round(total, 2)} and the average price of the items are R{round(average, 2)}")
