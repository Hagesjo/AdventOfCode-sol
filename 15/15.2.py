import re
permuts = []
# Stupid bruteforce
for a in range(1,100):
	for b in range(1,100):
		for c in range(1,100):
			d = 100-a-b-c
			if d > 0:
				permuts.append([a,b,c,d])

stuff = []

with open('input') as f:
	for line in f:
		regex = r'\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
		for cap, dur, flav, tex, cal in re.findall(regex, line):
			stuff.append(map(int, [cap,dur,flav,tex,cal]))

max_val = 0

for setup in permuts:
	sums = [0] * len(zip(*stuff))
	for index, value in enumerate(setup):
		sums = [x+y*value for x,y in zip(sums, stuff[index])]
	sums = map(lambda x: max(0,x), sums)
	if sums[-1] != 500:
		continue
	max_val = max(max_val, reduce(lambda x,y: x*y, sums[:-1]))

print max_val
