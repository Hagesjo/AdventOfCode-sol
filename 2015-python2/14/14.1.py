class Deer:
	def __init__(self, speed, flytime, rest):
		self.speed = speed
		self.flytime = flytime
		self.rest = rest

	def fly(self):
		distance = 0
		seconds_left = 2503
		while seconds_left:
			distance += self.speed * min(self.flytime, seconds_left)
			seconds_left -= min(seconds_left, self.flytime)
			seconds_left -= min(seconds_left, self.rest)
		return distance

deers = []
with open('input') as f:
	for line in f:
		_, _, _, speed, _, _, flytime, _, _, _, _, _, _, rest, _ = line.split()
		deers.append(Deer(*map(int, [speed,flytime,rest])))
		print max(map(lambda x: x.fly(), deers))
