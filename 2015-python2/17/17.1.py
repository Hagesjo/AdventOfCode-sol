from itertools import combinations
import itertools

containers = []
with open('input') as f:
	for line in f:
		containers.append(int(line))

results = []
for i in xrange(1,len(containers)+1):
	for c in combinations(containers, i):
		if sum(c) == 150:
			results.append(c)

print len(results)
