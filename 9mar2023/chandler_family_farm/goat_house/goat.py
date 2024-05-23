print( "maa maa" )
print( "give me some hay!")

class goat_house:
	
	def __init__(self, n_goats ):

		self.number_of_goats = n_goats
		self.floor_area_in_m2 = 3.0
		return 
		
	def print_info(self):
		print( "there are " + str(self.number_of_goats) + " goats in this house")
		print( "floor area in m2 = " + str(self.floor_area_in_m2))
		return 

g = goat_house(9)
g.print_info()
