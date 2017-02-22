from zombie import Zombie
import hero

# make a zombie object from the class
zombie_object = Zombie(6, 8, 10, 'bat', 15);

# ugly version of print that gives you all info
print dir(zombie_object)
# printing your variables
print vars(zombie_object)

# make a hero object from the hero class
hero1 = hero.Hero();

hero.cheer_hero(hero1);

heroObject = hero.Hero();
heroObject.cheer_hero();