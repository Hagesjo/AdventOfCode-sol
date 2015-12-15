def check_word(word):
	# I know that the regex solution is the way to go, but I wanted to solve it without regex
	triletter = False
	pair = False
	for index, c1, c2, c3 in zip(range(len(word)), word, word[1:], word[2:]):
		if not triletter: # Don't need to check if this has already been found
			if c1 == c3:
				triletter = True
		if not pair: # Don't need to check if this has already been found
			if (c1, c2) in zip(word[index+2:], word[index+3:]):
				pair = True
	return triletter and pair


with open('input') as f:
	total = 0
	for line in f:
		if check_word(line):
			total += 1
	print total
