import sys

def blank (test):
	for l in test:
		if l.strip():
			yield l

def decipher(test):
	tests = test.split(";")
	words = tests[0].split(" ")
	order = tests[1].split(" ")
	answer = [x for x in range(len(words))]
	missing = len(words) - len(order)

	for i, j in enumerate(order):
		answer[int(j)-1] = str(words[i])
	
	for i, j in enumerate(answer):
		if type(j) is int:
			answer[i] = str(words[-missing])
			missing -= 1
			
			
	print " ".join(answer)

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as test_cases:
		for test in blank(test_cases):
			decipher(test)
