def calculate_rim(dims):
	dims.sort()
	a,b,c= dims
	return 2*a + 2*b + a*b*c

with open('input') as f:
	for line in f:
		sum([calculate_rim(map(int,line.split('x'))) for line in f])
