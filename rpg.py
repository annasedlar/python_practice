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







# RPG Game

# You will base your game on version 5 of the game and make mods to the game.

# Characters

# make the hero generate double damage points during an attack with a probabilty of 20%
# make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
# make a character called Shadow who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
# make a Zombie character that doesn't die even if his health is below zero
# come up with at least two other characters with their individual characteristics, and implement them.
# Give each enemy a bounty. For example, the prize for defeating the Goblin is 5 coins, for the Wizard it is 6 coins.
# Items

# make a SuperTonic item to the store, it will restore the hero back to 10 health points.
# add an Armor item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
# add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
# come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.
# Bonus

# allow items to be used on the battle field. The hero can carry the items with him, and you have the option of choosing to use a tonic at any turn in a battle.
# make a Swap item, which when used on a battle field, will swap the power values of the two characters for one turn.
# there is a bug in the store that allows the hero to buy items even if he has no coins. Fix this bug.

