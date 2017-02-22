import time

class Hero(object):
	def __init__(self):
		self.name = "Incognito"
		self.health = 10
		self.power = 5

	#make an alive method that returns whether the hero is alive or not 
	def alive(self):
		# will return a boolean (T if this object's health > 0, F is this object's health <=0)
		return self.health > 0;
		
	def attack(self, enemy)
		print "%s attacks %s" % (self.name, enemy.name)
		enemy.take_damage(self.power);
		time.sleep(1.5); 
		print "%s has done %d damage to %s" % (self.name, self.power, enemy.name);

	def take_damage(self, points_of_damage):
		self.health -= points_of_damage;