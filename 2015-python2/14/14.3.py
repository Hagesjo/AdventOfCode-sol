def move_generator(speed, flytime, rest):
	distance = 0
	while True:
		for i in range(flytime, 0, -1):
			distance += speed
			yield distance
		for i in range(rest, 0, -1):
			yield distance

deers = {}
points = {}

with open('input') as f:
	for line in f:
		name, _, _, speed, _, _, flytime, _, _, _, _, _, _, rest, _ = line.split()
		deers[name] = move_generator(*map(int, [speed,flytime,rest]))
		points[name] = 0
	for i in range(2503):
		maxd = max([dist for dist in deers.values()])
		for deer in deers:
			if deer.distance == maxd:
				deer.points +=1

	print max(map(lambda x: x.points, deers))
