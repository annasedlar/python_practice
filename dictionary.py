# dictonary is the fancy python term for a JS object
# syntax is a bit different. 
# must put keys (properities) in ""
# called key-value pairs in python (property, value)

zombie = {
	'speed':10,
	'power':6,
	'hunger':12,
	'name':'Zombie'
}

# print zombie.speed => WRONG
print zombie['speed']; 

# add a new key just like you do in JS. vars are dynamic in python!
zombie['weapon'] = "fist"; 
zombie['startX'] = 200; 
zombie['startY'] = 100; 
print zombie

# change the value of an exisiting key, just like JS
if zombie['speed'] < 5:
	zombie['position'] = zombie['startX'] + 2;
elif zombie['speed'] > 10: 
	zombie['position'] = zombie['startX'] + 4; 
else: 
	zombie['position'] = zombie['startX'] + 6; 


# you can delete a key with DEL 
zombie['pointless'] = 'duh';
del zombie['pointless'];
print zombie


# store all the techs we know in a dictionary and set the value from 1-10
skill1 = 'Assembly'
tech = {
	'javascript': 11,
	'html': 9, 
	'css': 10,  
	'react': 6,
	'redux': 4, 
	'C++': 0, 
	'SASS': 2, 
	'websockets': 3,
	'python': 2, 
	'MySQL': 3,
	'Express': 2, 
	'Node': 4, 
	'git': 5,
	'lolololololol': 10,
	skill1: 0
}
print tech

# for loops through dictionaries start with key (placeholder), value
# .items() because it's a dictionary, not a list
for key,value in tech.items(): 
	print key;
if zombie.has_key('mother-name'):
	print zombie['mother_name']; 

if zombie.has_key('SASS'):
	print zombie['SASS'];

for key in zombie:
	print zombie[key]

# you can mput dictionaries inside of lists ( objects in arrays)
zombies = [];
zombies.append({
	'speed': 10, 
	'power': 6, 
	'hunger': 5, 
	'name': 'Bill'
	})
zombies.append({
	'speed': 5, 
	'power': 16, 
	'hunger': 9, 
	'name': 'Sven'
	})
print zombies
print zombies[0]
print zombies[0]['name']

for zombie in zombies: 
	print zombie['name']

# just like js objects, you can assign a list to a dictionary key

zombies[0]['victims'] = ['sean', 'rishi', 'anna'];
print zombies[0];

print zombies[0]['victims'][0];

zombies[0]['victims'][0]['name'] = "sean";
print zombies[0];

zombie[0]['at_night'] = {
	# at night
	'power': 23, 
	'hunger': 20,
	'weapon': 'baseball bat'
}











