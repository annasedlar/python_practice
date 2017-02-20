print "Anna Sedlar"

name = "Anna Sedlar" 

# lists = arrays
animals = ['wolf', 'giraffe', 'hippo']
print animals

# this will go one from the end of the array ie. hippo
print animals[-1] 

# array.push == list.append
animals.append("Alligator");
print animals

# to delete an index, use remove method
animals.remove('wolf'); 
print animals

# alternatively, use del
del animals[0];

# insert into any idicie with 'insert'
animals.insert(0, 'zebra');
print animals

animals[0] = 'horse'; 
print animals

# pop works like js pop - removes last element of a list
animals.pop()
print animals
animals.pop()
print animals





dc_class = "Michael, Paul, Mason, Casey, Connie, Sarah, Andy"; 
dc_class_as_array = dc_class.split(", "); 
print dc_class_as_array

# sorted method will sort, but NOT CHANGE the actual array
print sorted(dc_class_as_array); 

# so you must assign it a variable
sorted_class = sorted(dc_class_as_array)

dc_class_as_array.sort()
print dc_class_as_array
print sorted
print dc_class_as_array

# reverse method reverse the array not by value but by index
dc_class_as_array.reverse();
print dc_class_as_array;

# length
print len(dc_class_as_array)

# slice [x:x]
# creates a copy of the array, does not mutate the array
print dc_class_as_array[2:4]

for student in dc_class_as_array:
	print student

for i in range(1, 10):
	print i; 

for i in range(1, len(dc_class_as_array)):
	print dc_class_as_array

# A function in python is NOT a function. It is a definition (def) 
def say_hello():
	# just like for loops, colon is the curly brace in python for functions
	# indentation matters, just like for loop
	print "Hello World"; 

say_hello(); 

def say_hello_with_name(name): 
	print "hello, " + name; 

# MUST pass at least correct num of args - ie. if you pass two, it'll only take the first
say_hello_with_name("Anna"); 










