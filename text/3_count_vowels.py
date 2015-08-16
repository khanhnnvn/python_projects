# Enter a string and do 2 things:
# 1. Count the number of vowels in the string
# 2. Count the number of occurences for each vowel

# Ask the user to enter a string
print "Enter any string to count vowels:"
inStr = raw_input("> ")

# Store all vowels and their occurences in a dict
# Key: the vowel itself. Value: number of occurences
vowels = {}

# Variable to store total number of vowels
total_vowels = 0

# Function to check whether a character is a vowel
def isVowel(char):
	return char in ['a', 'e', 'o', 'i', 'u']

# Check each character in the string. 
# If it's a vowel and already in "vowels" dict, increase its value
# Otherwise, add an entry to "vowels" dict
# In both cases, increase the total number of vowels found
for ch in inStr:
	if isVowel(ch):	
		total_vowels += 1		# also increase the number of vowels along the way
		if ch in vowels.keys():
			vowels[ch] += 1
		else:
			vowels[ch] = 1

# print the result
print "Results:"
print vowels
print "Number of vowels:", total_vowels