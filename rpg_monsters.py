class Goblin(object):
	def __init__(self):
		self.name = "goblin"
		self.health = 6
		self.power = 2

	#make an alive method that returns whether the goblin is alive or not 
	def alive(self):
		# will return a boolean (T if this object's health > 0, F is this object's health <=0)
		return self.health > 0
		
	def take_damage(self, points_of_damage):
		self.health -= points_of_damage;

	def attack(self, hero):
		print "%s attacks %s" % (self.name, hero.name)
		hero.take_damage(self.power); 