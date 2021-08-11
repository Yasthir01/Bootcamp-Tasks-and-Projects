"""A program for a courier company to calculate the cost of sending a parcel"""



# ask the user to enter the price of the package they would like to purchase
package_price = float(input("Please enter price of package: "))
# the user to enter total distance of the delivery in kilometres
distance = float(input("Please enter in the distance of the delivery (KM): "))

""" Now we need to add on delivery costs to the final cost of the product
	 we need to take 4 categories into account, each with 2 options"""

# create variables that will be used in options
delivery_air = 0.36  # $0.36 per km
freight = 0.25  # $0.25 per km

full_insurance = 50.00
limited_insurance = 25.00

gift = 15.00
no_gift = 0.00

priority_delivery = 100.00
standard_delivery = 20.00


""" The user will be asked to make a choice in 4 categories and they will have to choose between 2 options."""

choice1 = input("Delivery via 'Air' ($0.36 per km) or 'Freight' ($0.25 per km) - Type in 'Air' or 'Freight': ")
choice2 = input("Full Insurance ($50.00) or Limited Insurance ($25.00) - Type in 'Full' or 'Limited': ")
choice3 = input("Gift Option ($15.00) or Not Gift ($0.00) - Type in 'Gift' or 'No': ")
choice4 = input("Priority Delivery ($100.00) or Standard Delivery ($20.00) - Type in 'Priority' or 'Standard': ")


""" We now need to determine what happens once the choices are made """

# mode of transport
if choice1 == 'Air':
	transport_price = delivery_air * distance
else:
	transport_price = freight * distance


# choice of insurance
if choice2 == 'Full':
	insurance_price = full_insurance
else:
	insurance_price = limited_insurance


# gift or not
if choice3 == 'Gift':
	gift_price = gift 
else:
	gift_price = no_gift


# priority or standard delivery
if choice4 == 'Priority':
	delivery_price = priority_delivery
else:
	delivery_price = standard_delivery


# total price of order
total = package_price + transport_price + insurance_price + gift_price + delivery_price
print(f"The total amount for your order is : {total}")


