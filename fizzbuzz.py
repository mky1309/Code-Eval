import sys

def rmvBlankLines(test):
	for l in test:
		if l.strip():
			yield l

def fizzbuzz(test):
	tests = test.split(" ")
	f = int(tests[0])
	b = int(tests[1])
	n = int(tests[2])
	answer = []

	for i in range(1, n+1):
		if i % f == 0 and i % b == 0:
			answer.append("FB")
		elif i % f == 0:
			answer.append("F")
		elif i % b == 0:
			answer.append("B")
		else:
			answer.append(str(i))
	
	print " ".join(answer)

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as test_cases:
		for test in rmvBlankLines(test_cases):
			fizzbuzz(test)
		
