class Presentdealer:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.houses = set()
		self.houses.add((self.x,self.y))

	def move(self,c):
		if c == '<':
			self.x -= 1
		if c == '>':
			self.x += 1
		if c == 'v':
			self.y -= 1
		if c == '^':
			self.y += 1
		self.houses.add((self.x,self.y))

with open('input') as f:
	santa = Presentdealer()
	robo = Presentdealer()
	for index, c in enumerate(f.read()):
		if index % 2 == 0:
			santa.move(c)
		else:
			robo.move(c)
		
	print len(robo.houses.union(santa.houses))
