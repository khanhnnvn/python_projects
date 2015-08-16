# Check whether a string is a palindrome
# A string is called palindrome if it's exactly the same both original and backward

# Ask for user to enter a string to check for palindrome
print "Enter a string to check whether it's palindrome:"
inStr = raw_input("> ")

# Reverse the input string. For raw implementation, see 1_reverse_a_string.py
reverseStr = inStr[::-1]

# Check whether both strings are exactly same
if (inStr == reverseStr):	# yes? 
	print "===> %s is a palindrome." % inStr
else:	# not same
	print "===> %s is not a palindrome." % inStr