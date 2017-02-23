class Animal(object): 
	def __init__(self, name, species):
		self.name = name; 
		self.species = species
	def speak(self):
		print self.name + " is making a noise!"; 

	def run(self):
		print self.name + " is running"; 

animal1 = Animal("Mitze", "alien"); 
animal1.speak(); 
animal1.run();


# make a new class. instead of passing object/nothing, we pass name of parent class
class Dog(Animal): 
	def __init__(self, dogName): 
		# sends up parameters to parent
		Animal.__init__(self, dogName, "Dog");
		print self.name;
	def bark(self):
		print self.name + " is barking!"

dog  = Dog("Roofus")
dog.bark()
print dog.species;











