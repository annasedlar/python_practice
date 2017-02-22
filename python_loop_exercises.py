# 1 to 10
# Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line. Example output:
# $ python 1_to_10.py
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for numbers in range (0, 11):
# 	print numbers


# n to m
# Same as the previous except you will prompt the user for the number to start on and the number to end on. Example session:
# $ python n_to_m.py
# Start from: 2
# End on: 8
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# start = int(raw_input("give me a number to start on: "));
# end = int(raw_input("give me a number to end on: ")); 
# for numbers in range(start, end +1):
# 	print numbers



# Odd Numbers
# Print each odd number between 1 and 10 inclusive. Example output:
# $ python odd_numbers.py
# 1
# 3
# 5
# 7
# 9
# Hint: you will need to use the modulus operator % to determine whether a number is odd or even.
# for i in range (1, 11):
# 	if i % 2 != 0:
# 		print i




# Print a Square
# Print a 5x5 square of * characters. Example output:
# $ python square.py
# *****
# *****
# *****
# *****
# *****

# for index in range (0, 5):
# 	print ("******")






# Print a Square II
# Print a NxN square of * characters. Prompt the user for N. Example output:
# $ python square2.py
# How big is the square? 10
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

# length = int(raw_input("What height/length do you want your square to be?: "))
# for i in range (0, length):
# 	print("*" * length)







# Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border.
# Example session:
# $ python box.py
# Width? 6
# Height? 4
# ******
# *    *
# *    *
# ******

# height = int(raw_input("Give me a box height: "))
# width = int(raw_input("And a box width: "))
# print ("*" * width)
# for i in range(0, (height - 2)):
# 	print("*" + (" " * (width - 2)) + "*")
# print ("*" * width)









# Print a Triangle
# Print a triangle consisting of * characters like this:
#    *
#   ***
#  *****
# *******

# &&

# Print a Triangle II
# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.

height = int(raw_input("give me a height: "))
i = 0
level = 1
base = ((2 * height )-1)
stars = '*';
space = ' ';
while i < height:
	num_of_init_spaces = ((base - level) /2)
	# print num_of_init_spaces + "*"
	print (space* num_of_init_spaces) + (stars*level)
	level += 2 
	i += 1




# Multiplication Table
# Print the multiplication table for numbers from 1 up to 10. Example output:
# $ python multiplication_table.py
# 1 X 1 = 1
# 1 X 2 = 2
# 1 X 3 = 3
# 1 X 4 = 4
# ...
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# ...
# 10 X 8 = 80
# 10 X 9 = 90
# 10 X 10 = 100







# Bonus: Print a Banner
# Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string.
# Example session:
# $ python banner.py
# Text? Welcome to DigitalCrafts
# ****************************
# * Welcome to DigitalCrafts *
# ****************************







# Bonus: Triangle Numbers
# Print the first 100 triangle numbers. What is a triangle number? Read this:
# https://www.mathsisfun.com/algebra/triangular-numbers.html.








# Bonus: Factor a Number
# Given a number, print its factors. What are factors?
# https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-and-factors/v/finding-factors-of-a-number









