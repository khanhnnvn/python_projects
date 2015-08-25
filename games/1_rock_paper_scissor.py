# This program simulates the Rock Paper Scissor Game. User input vs Computer
# Rules:
# 	- Paper wins Rock
# 	- Rock wins Scissor
# 	- Scissor wins Paper

import random as rd

def main():
	# Variables to keep track of scores
	comWin = 0
	userWin = 0

	while True:
		# Current score
		print "\n======== USER %d - %d COMPUTER ========" % (userWin, comWin)

		# Ask for user input
		print "What's your choice?"
		print "== r for Rock"
		print "== s for Scissor"
		print "== p for Paper"
		userInput = raw_input("> ").lower()
		# If user does not enter either 'r', 'p' or 's', inform him
		if userInput != 'r' and userInput != 's' and userInput != 'p':
			print "Wrong input. Must be either 'r' or 's' or 'p'"
			continue

		# This dict maps computer randomly generated number to specific choice
		choices = {1: 'r', 2: 's', 3: 'p'}
		# This dict maps the shortcut character input by user or computer to corresponding choice
		realChoices = {"r": "Rock", "s": "Scissor", "p": "Paper"}
		# Randomly generated a number between 1 to 3 to simulate computer's choice
		comInput = rd.randint(1,3)

		print "You choose: %s. Computer choose: %s" % (realChoices[userInput], realChoices[choices[comInput]])
		# Get result
		r = result(userInput, choices[comInput])
		if r == 'd':
			print "Draw"
		elif r =='c':
			print 'Haha! Computer wins.'
			comWin += 1
		else:
			print 'Congratulation! You win!'
			userWin += 1

# This function takes user and computer input and return 'u', 'c' or 'd'
# 'u' means User wins. 'c' means Computer wins. 'd' means Draw
def result(userInput, comInput):
	# If both are same, return Draw
	if userInput == comInput:
		return 'd'
	# If user choose Rock
	else:
		if userInput == 'r':
			if comInput == 'p':
				return 'c'
			else:
				return 'u'
		elif userInput == 'p':
			if comInput == 'r':
				return 'u'
			else:
				return 'c'
		else:	# userInput == 's'
			if comInput == 'r':
				return 'c'
			else:
				return 'u'
	
if __name__ == "__main__":
	main()