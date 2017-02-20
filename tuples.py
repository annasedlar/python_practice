# a list is great, but it's mutable. if you want something immutable, use a tuple

a_tuple = (1,3,8)
print a_tuple;
print a_tuple[2];

# loop through tuples the same way you loop through lists
# tuples cannot be changed 
# tuples use parentheses, not brackets like lists
for number in a_tuple:
	print number;

teams = ('falcons', 'hawks', 'redwings', 'tigers');
if teams[0] == 'falcons':
	print "woo";
else:
	print "boo";

team_a = "falcons";
print team_a == 'falcons'; 
# will print true

team_b = 'braves'; 
if team_a == 'falcons' and team_b == 'braves': 
	print "hooray!"; 

cond1 = team_a =='falcons'
cond2 = team_b =='braves'
if cond1 and cond2: 
	print 'woohoo';

# python's version of indexOf is "in"

print 'redwings' in teams;

for team in teams: 
	if team == 'redwings': 
		print 'Go Wings';
	elif team == 'tigers':
		print "Rwawr";

if 'redwings' in teams: 
	print "Go Hawks"; 
elif 'tigers' in teams: 
	print "go tigers";



# message = raw_input("Please enter your name"); 
# height = raw_input("how tall are you (in inches) \n")
# if(int(height) >= 42): 
# 	print "You are tall enough to go on the Batman roller coaster"; 
# else: 
# 	print "You're too short! Maybe try the kiddie coaster.";



# # WHILE LOOP
# # current = 1;
# # while current < 10: 
# # 	print current; 
# # 	current +=1; 

# answer = 'play';
# while answer != 'quit': 
# 	answer = raw_input("say quit to stop the game \n");


# make a number guessing game
import random
rando = random.random(); 
print rando
rando2 = int(rando * 10) + 1
print rando2
prompt = raw_input("I've got a number between 1 and 10 - can you guess it? \n");
if prompt == rando2:
	print "You guessed right!"; 
else: print "Wrong. My number was actually " + str(rando2);












