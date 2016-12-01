from PIL import Image

class Presentdealer:
	def __init__(self, color):
		self.x = 0
		self.y = 0
		self.houses = set()
		self.houses.add((self.x,self.y))
		self.color = color

	def move(self,c):
		if c == '<':
			self.x -= 1
		if c == '>':
			self.x += 1
		if c == 'v':
			self.y -= 1
		if c == '^':
			self.y += 1
		pixels[500 + self.x*2,500 + self.y*2] = self.color
		self.houses.add((self.x,self.y))

with open('input') as f:
	img = Image.new('RGB', (1000, 1000))
	pixels = img.load()
	santa = Presentdealer((255, 0, 0))
	robo = Presentdealer((0, 255, 0))
	for index, c in enumerate(f.read()):
		if index % 2 == 0:
			santa.move(c)
		else:
			robo.move(c)
	img.save('3.2.png')
		
	print len(robo.houses.union(santa.houses))

