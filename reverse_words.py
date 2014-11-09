import sys

def blank (test):
	for l in test:
		if l.strip():
			yield l.strip()

def reverse(test):
	sentence = test.split(" ")
	sentence.reverse()

	print " ".join(sentence)

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as test_cases:
		for test in blank(test_cases):
			reverse(test)
	
