# This program produces a Pig Latin from an original word
# Here are the rules:
# If the word starts with 1 or more consonants, move all consonants to the end and suffix "ay"
# If the word starts with a vowel, just add "way" to the end

# Use regular expression to check whether word begins with a vowel
# or with one or more consonant
import re 	

# Ask user to enter a string
print "Enter a word to convert to Pig Latin:"
inStr = raw_input("> ")

# Result stored here
pigLatin = ""

# Function to check whether a character is a vowel
# Used to check the first character of the word
#def isVowel(ch):
#	return ch in ['a', 'e', 'i', 'u', 'o']

# Check if word begins with a vowel
matchGroup = re.match(r'[aiuoe]', inStr)

# If yes, then just add "way" to the end
if matchGroup:
	pigLatin = inStr + "way"
else:	# otherwise
	# seach for consonant(s)
	matchGroup = re.match(r'[^aiuoe]{1,}', inStr)
	# move all consonants to the end, and add "ay"
	pigLatin = inStr.replace(matchGroup.group(), "") + matchGroup.group() + "ay"

# print the result
print "Here's your Pig Latin:"
print ">", pigLatin