# Read from a file and count total number of words.
# Also count occurences of each word. Spaces excluded.

from sys import argv
from sys import exit

# Notify user if he didn't give the file name
if len(argv) < 2:
	print "You must input a file name also!"
	print "Usage: python 5_count_words.py <file_name_to_count>"
	exit(0)

# get file name from argument parameters
script, FILE = argv
inFile = open(FILE)		

# word dictionary
words = {}

# read the file line by line and keep track of occurences for each word
for line in inFile.readlines():
	wordsInLine = line.split(' ')
	for word in wordsInLine:
		word = word.strip('.,\\/\t\n)(}{')	# strip weird chars from word
		if word not in words.keys(): 				# if word not already exists in dictionary, add it
			words[word] = 1
		else:																# otherwise, increase current count for that word
			words[word] += 1

# close opened file
inFile.close()

# print the result
for word in words.keys():
	print "%s\t%s" % (word, words[word])
print "Total words:", sum(words.itervalues())