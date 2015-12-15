with open('input') as f:
	print sum(len(line[:-1]) - len(eval(line)) for line in f)
	print sum(2+line.count('\\')+line.count('"') for line in f)

