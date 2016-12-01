from PIL import Image
from random import randint
# Generate image
img = Image.new('RGB', (1000, 1000))
pixels = img.load()
for i in range(1000):
	for j in range(1000):
		value = lights[i][j] * 3
		pixels[i,j] = (randint(0, 255), randint(0, 255), randint(0,255))
img.save('kul.png')

