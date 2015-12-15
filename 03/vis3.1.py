from PIL import Image

def rainbow():
  r, g, b = 255, 0, 0
  for g in range(256):
    yield r, g, b
  for r in range(255, -1, -1):
    yield r, g, b
  for b in range(256):
    yield r, g, b
  for g in range(255, -1, -1):
    yield r, g, b
  for r in range(256):
    yield r, g, b
  for b in range(255, -1, -1):
    yield r, g, b

a = list(rainbow())
print a

with open('input') as f:
	houses = set()
	x = 0
	y = 0
	step = 0
	houses.add((x,y))
	img = Image.new('RGB', (1000, 1000))
	pixels = img.load()
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
		pixels[500 + x*3,500 + y*3] = a[step % len(a)-1]
		step += 1
	img.save('test.png')
	print len(houses)
