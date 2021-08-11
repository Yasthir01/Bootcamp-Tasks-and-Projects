"""Inheritance in Python"""


class Animal(object):

	def __init__(self, numteeth,spots,weight):
		self.numteeth = numteeth
		self.spots = spots
		self.weight = weight


class Lion(Animal):

	def __init__(self, numteeth, spots, weight):
		super().__init__(numteeth, spots, weight)
		self.type()


	def type(self):
		"""Determine type of lion based on weight"""
		if self.weight < 80:
			self.lion_type = 'Cub'
		elif self.weight < 120:
			self.lion_type = 'Female'
		elif self.weight > 120:
			self.lion_type = 'Male'


class Cheetah(Animal):
	def __init__(self, numteeth, spots, weight, prey):
		super().__init__(numteeth, spots, weight)
		self.prey = prey



# lion object
lion1 = Lion(30, 0, 130)
print(lion1.lion_type)

# cheetah object
cheetah = Cheetah(20, 5, 100, ['Buffalo', 'Gazelle'])
print(cheetah.prey)
