# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.

full_name = "Anna Sedlar"; 
age = 24; 


# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.

my_array = [];
my_array.insert(0, full_name);
my_array.insert(1, age);
print my_array;


# 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.

def sayHello():
	print "Hello!";
sayHello(); 

# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed in the instructions PDF.

split_name = full_name.split(); 
print split_name; 


# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)

def say_name(name): 
	print "Hello " + name + "!";

say_name("Anna"); 


# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.
# HINT: http://www.w3schools.com/js/js_functions.asp
 
import datetime
from datetime import date
print date.today()
def my_age(birthyear): 
	today = date.today()
	print today.year - birthyear

my_age(1992); 

# 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console
# the sum of all the odd numbers from 1 to 5000.  Don't forget to call the function!
# HINT: Consider using a 'for loop'.
 
# function sum_odd_numbers() {
#     var sum = 0;

#     // Write your code here
#     console.log(sum);
# }

def sum_odd_numbers(): 
	count = 0 
	for i in range(1, 5000): 
		if i % 2 == 1:
			count += i;  
	print(count); 

sum_odd_numbers();


# OR USE STEP PARAM
def sum_odd_nums2():
	sum = 0
	# third param = STEP
	for i in range(1, 5000, 2):
		sum += i; 
	print(sum); 

sum_odd_nums2(); 






