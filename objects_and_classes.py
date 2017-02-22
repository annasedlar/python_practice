class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

# Write code to:
# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# Have sonny greet jordan using the greet method.
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan.

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948');
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456');

jordan.greet(sonny);
sonny.greet(jordan);
print 'Sonny contact info: %s, %s' % (sonny.email, sonny.phone)
print 'Jordan contact info: %s, %s' % (jordan.email, jordan.phone)


# Create a class Vehicle. A Vehicle object will have 3 attributes:
# make
# model
# year
# A vehicle is created thus:

class Vehicle(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	def print_info(self):
		print " %s %s %s" % (self.year, self.make, self.model)

# Add a print_info method to the Vehicle class. 
# It will print out the vehicle's information like so:
# >>> car.print_info()
# 2015 Nissan Leaf

car = Vehicle('Nissan', 'Leaf', 2015)
print car.make

car.print_info();


























