# Sum the Numbers
# Given an list of numbers, print their sum. When I say given something, just make something up and store it in a variable.
# list = [4, 3, 7, 8, 10, 60, -9]
# print sum(list)

# # Largest Number
# # Given an list of numbers, print the largest of the numbers.
# print max(list)

# # Smallest Number
# # Given an list of numbers, print the smallest of the numbers.
# print min(list)

# Even Numbers
# Given an list of numbers, print each number in the list that is even.
# def even(list):
# 	for number in list:
# 		if number % 2 == 0:
# 			print number; 
# even(list)


# Positive Numbers
# Given an list of numbers, print each number in the list that is greater than zero.
# def positive(list):
# 	for number in list:
# 		if number > 0:
# 			print number; 
# positive(list)


# Positive Numbers II
# Given an list of numbers, create a new list which contains every number in the given list which is positive.
# def pos(list):
# 	new_list = []
# 	for number in list: 
# 		if number > 0:
# 			new_list.append(number); 
# 			print(new_list)
# pos(list); 


# Multiply an list
# Given an list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers
# in the first list multiplied by the factor. Print this list using console.log(list);
# def mult_by_two(list):
# 	new_list = []
# 	for number in list: 
# 		times_two = number * 2
# 		new_list.append(times_two); 
# 		print(new_list)
# mult_by_two(list); 


# Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in
# corresponding positions in the two lists. Example:
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# new_array = []
# def mult_vect(list1, list2):
# 	for i in range(0, len(list1)): 
# 		new_array.append(list1[i]*list2[i])
# 		print new_array
# mult_vect(list1, list2)


# Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
# [ [2, -2], [5, 3] ]

# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be
# the sum of the numbers in the corresponding addend matrices. Example: to add
# 1 3
# 2 4
# and
# 5 2
# 1 0
# results in
# 6 5
# 3 4

list1 = [[1, 2],[3.4]]
list2 = [[1, 2], [3,4]]
def matrix_add(list1, list2):
	new_array = []
	for i in range(0, len(list1)):
		for j in range(0, len(list1[0])):
			new_array.append(list1[0][i] + list2[0][j])
			new_array.append(list1[1][i] + list2[1][j])
			print new_array
			print len(list1)
matrix_add(list1, list2)







# Matrix Addition II

# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.

# De-dup

# Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

# Bonus: Matrix Multiplication

# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices.
# Print the resulting matrix. How do you multiple two matricies? 
# https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro














