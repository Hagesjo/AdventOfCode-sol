VOWELS = "aeiou"
N_STRINGS = ["ab", "cd", "pq", "xy"]

def check_word(word):
	# I know that the regex solution is the way to go, but I wanted to solve it without regex
	vow = 0
	doublechar = False
	for c, c2 in zip(word, word[1:]):
		if not doublechar: # Don't need to check this if a doublechar has been found
			if c == c2:
				doublechar = True
		if c + c2 in N_STRINGS:
			return False
		if c in VOWELS:
			vow += 1
	return doublechar and vow >= 3

with open('input') as f:
	total = 0
	for line in f:
		if check_word(line):
			total += 1
	print total
