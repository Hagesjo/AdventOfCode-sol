with open('input') as f:
	houses = set()
	x = 0
	y = 0
	houses.add((x,y))
	for c in f.read():
		if c == '<':
			x -= 1
		if c == '>':
			x += 1
		if c == 'v':
			y -= 1
		if c == '^':
			y += 1
		houses.add((x,y))
	print len(houses)
