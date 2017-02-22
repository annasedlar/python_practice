class Hero(object): 
	def __init__(self): 
		self.name = "Anna";

		# this is a member function of the hero class, local
	def cheer_hero(self):
		print "Fight hard, " + self.name + " !";


# this is a global function
def cheer_hero(hero):
	print "global"; 