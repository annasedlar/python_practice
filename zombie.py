class Zombie(object):
	def __init__(self, speed, strength, hunger, weapon, health):
		self.speed = speed;
		self.strength = strength;
		self.hunger = hunger; 
		self.weapon = weapon; 
		self.health = health; 
		self.type = 'zombie'; 

# zombie_object = Zombie(6, 8, 10, 'bat', 15);
# print zombie_object;
# print zombie_object.strength;
# print zombie_object.type;

# # prints all functions, including member functions
# print dir(zombie_object);

# # prints only the functions you've created
# print vars(zombie_object); 

