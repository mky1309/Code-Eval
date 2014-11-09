import sys
from operator import itemgetter

def longest_lines():
	with open(sys.argv[1], 'r') as f:
		number = int(f.readline())
		words = []
		length = []
		x = 1
		
		for line in f:
			line.rstrip()
			words.append(line)
		
		for i in words:
			length.append(len(i))

		order = zip(words, length)

		sorted_words = sorted(order, key=itemgetter(1), reverse=True)
		
		while x <= number:
			print sorted_words[x-1][0],
			x += 1
			
		
		
if __name__ == "__main__":
	longest_lines()
