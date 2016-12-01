from PIL import Image
import operator
from itertools import groupby
import sys


class Rect:
	def __init__(self,sx, sy, ex, ey):
		self.sx = sx
		self.ex = ex
		self.sy = sy
		self.ey = ey
	
	def __repr__(self):
		return "%s %s %s %s\n" % (self.sx, self.sy, self.ex, self.ey)

def main():
	if len(sys.argv) != 2:
		print "Usage: python instruct_generator.py infile"
		exit(1)
	a = Image.open(sys.argv[1])
	pixels = list(a.getdata())
	width, height = a.size
	pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

	rects = []
	for index, row in enumerate(pixels):
		p = filter(lambda x: x[1] == (0,0,0), enumerate(row))
		if not p:
			continue
		p = map(lambda x: x[0], p)
		p = [(v, v-i) for i, v in enumerate(p)]
		for k,v in groupby(p, operator.itemgetter(1)):
			v = list(v)
			rects.append(Rect(v[0][0], index, v[-1][0], index))

	with open('gen_input.txt', 'w') as f:
		for rect in rects:
			f.write("turn on %s,%s through %s,%s\n" % (rect.sx, rect.sy, rect.ex, rect.ey))
		f.write("toggle 0,0 through 999,999")

if __name__=="__main__":
	main()
