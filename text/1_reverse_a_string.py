# This program asks user to input a string and reverse it

# Ask user to enter a string
print "Input any string to reverse:"
inStr = raw_input("> ")

# Initialize reversed string
reverseStr = ""

# Access input string character by character from last, append to the output string
currentIndex = len(inStr) - 1
while currentIndex >= 0:
	reverseStr += inStr[currentIndex]
	currentIndex -= 1

# Print out
print "Here's your reversed string: "
print ">", reverseStr