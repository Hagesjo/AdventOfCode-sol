def calculate_area(dims):
	dims.sort()
	l,w,h = dims
	return 3*l*w + 2*w*h + 2*h*l # *3 since slack

total = 0
with open('input') as f:
	for line in f:
		total += calculate_area(map(int,line.split('x')))
print total
