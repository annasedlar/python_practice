from rpg_hero import Hero;

from rpg_monsters import Goblin; 

hero = Hero(); 
enemies = [Goblin()];

for enemy in enemies:
	# loop through all bad guys in enemies list
	print vars(enemy);
	# while hero.health > 0 and enemy.health > 0:
	while hero.alive and enemy.alive:
		print "what will you do?";
		print "1. Fight %s" % enemy.name
		print "2. Run Away";
		print "> ", 
		input = raw_input();
		if int(input) == 1: 
			# enemy.health -= hero.power; 
			hero.attack(enemy);
		elif int(input) == 2: 
			break;
		else:
			print "Invalid choice %r" % input
		if enemy.alive():
			hero.health -= enemy.power; 
	if hero.alive():
		# we know they won beacuse someones health is < 0 
		print "you won! the %s is defeated!" % enemy.name
	else: 
		# we know the hero lost because someone won and it is not the hero
		print "you were defeated by the ferocious %s" % enemy.name




