"""Functions based on a holiday trip"""


def HotelCost(num_nights):
	"""Calculate the the total cost for the hotel stay"""
	price_per_night = 1000
	return num_nights * price_per_night


def PlaneCost(city):
	"""Calculate the cost of a flight based on location"""
	if city == 'Pietermaritzburg':
		cost = 400
	elif city == 'Durban':
		cost = 500
	elif city == 'Cape Town':
		cost = 700
	else:
		cost = 0
		print("There are no flights to that city")

	return cost 


def CarRental(num_days):
	"""Car rental price based on number of days used"""
	rental_price = 500  # 500 per day
	return num_days * rental_price


def HolidayCost(hotel, plane, car):
	"""Calculate total holiday cost"""
	hotel_cost = HotelCost(hotel)
	plane_cost = PlaneCost(plane)
	car_rental = CarRental(car)
	return hotel_cost + plane_cost + car_rental


# testing out a few examples
print(HolidayCost(5, 'Durban', 4))
print(HolidayCost(4, 'Cape Town', 3))
print(HolidayCost(2, 'Pietermaritzburg', 2))

# if the user enters a city that is not available
print(HolidayCost(3, 'Madrid', 3))  # still gives total without plane cost

