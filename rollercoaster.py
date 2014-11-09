import sys

def blank (test):
	for l in test:
		if l.strip():
			yield l

def rollercoaster(test):
	
	tests = test.split()
	counter = 1
	answer = []
	
	for l in test:
		if l.isalpha() and counter % 2 != 0:
			answer.append(l.upper())
			counter += 1
		elif l.isalpha():
			answer.append(l)
			counter += 1
		else:
			answer.append(l)
	

	print "".join(answer),

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as test_cases:
		for test in blank(test_cases):
			rollercoaster(test)
