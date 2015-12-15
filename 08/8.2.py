with open('input') as f:
	print sum(2+line.count('\\')+line.count('"') for line in f)
