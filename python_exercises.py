# # Uppercase a String
# # Given a string, print the string uppercased. #string #easy
# def to_string(string):
# 	print string.upper();
# to_string("hello");
# string = 'hello';
# print string.upper()

# # Capitalize a String
# # Given a string, print the string capitalized. #string #easy
# def cap(string):
# 	print string.capitalize();
# cap("hi my name is anna");

# # Reverse a String
# # Given a string, print the string reversed.
# def rev(string): 
# 	print string[::-1];
# rev("hi my name is anna")

# # Leetspeak
# # Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak,
# # you need to replace make the following character replacements (treat all input characters as uppercase):
# # A => 4
# # E => 3
# # G => 6
# # I => 1
# # O => 0
# # S => 5
# # T => 7
# # Example: Leet => l337
# word = raw_input("enter something to be converted to l33tsp34k:")
# leetmsg = word
# leetwords = 'aeuiotsu';

# for letter in word:
# 	if letter in leetwords:
# 		leetmsg = leetmsg.replace('a', "4")
# 		leetmsg = leetmsg.replace('e', "3")
# 		leetmsg = leetmsg.replace('i', str(1))
# 		leetmsg = leetmsg.replace('o', str(0))
# 		leetmsg = leetmsg.replace('t', str(7))
# 		leetmsg = leetmsg.replace('s', '$')
# 		leetmsg = leetmsg.replace('u', 'joo')
# print "Translated Message: ", leetmsg


# Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:
# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon
# Caesar Cipher

word = raw_input("give me a word: "); 
extensions = ["aaaa", "eeee", "iiii", "oooo", "uuuu"];
vowels = ['a', 'e', 'i', 'o', 'u'];
long_vowels = ["aa", "ee", "ii", "oo", "uu"];

for letter in word: 
	if word[letter] in vowels: 
		print "Yas there's a vowel"

# for letter in range(0, len(word)):
# 	if letter in long_vowels:
# 		print "translation: " + letter
# 	else: 
# 		print "no change"



# Given a string, print the Caesar Cipher (or ROT13) of that string.
# What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/
# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

















