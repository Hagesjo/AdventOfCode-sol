from PIL import Image

with open('input') as f:
	lights = [[0 for c in range(1000)] for line in range(1000)]
	for line in f:
		action, start_coord, _, end_coord = line.rsplit(' ', 3)
		start_x, start_y = map(int,start_coord.split(','))
		end_x, end_y = map(int,end_coord.split(','))
		for x in range(start_x, end_x + 1):
			for y in range(start_y, end_y + 1):
				lights[x][y] += {'turn off'	: -1 if lights[x][y] != 0 else 0,
								'turn on'	: 1,
								'toggle': 2}.get(action)
	print max(map(max, lights))

	# Generate image
	img = Image.new('RGB', (1000, 1000))
	pixels = img.load()
	for i in range(1000):
		for j in range(1000):
			value = lights[i][j] * 3
			pixels[i,j] = (value, value, value)
	img.save('image.png')
