def incr(inp):
	inp = inp[::-1]
	for index, value in enumerate(inp):
		if inp[index] == 'z':
			inp[index] = 'a'
		else:
			inp[index] = chr(ord(value) + 1)
			break
	return inp[::-1]


def validate(inp):
	if 'i' in inp:
		return False
	if 'o' in inp:
		return False
	if 'l' in inp:
		return False
	second = 0
	invalidateNext = False
	for a in range(len(inp[:-1])):
		if invalidateNext:
			invalidateNext = False
			continue
		if inp[a] == inp[a+1]:
			invalidateNext = True
			second += 1 
	if second < 2:
		return False
	for a in range(len(inp[:-2])):
		if ord(inp[a]) - ord(inp[a+1]) == -1 and ord(inp[a+1]) - ord(inp[a+2]) == -1:
			return True
	return False

with open('input') as f:
	for line in f:
		line = list(line.strip())
		while not validate(line):
			line = incr(line)
		first =  ''.join(line)
		print "first", first

		first = incr(list(first))
		while not validate(list(first)):
			first = incr(first)
		print ''.join(line)
