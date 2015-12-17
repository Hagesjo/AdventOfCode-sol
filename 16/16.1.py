import operator

class Aunt:
	def __init__(self, **kwargs):
		self.children = None
		self.cats = None
		self.samoyeds = None
		self.pomeranians = None
		self.akitas = None
		self.vizslas = None
		self.goldfish = None
		self.trees = None
		self.cars = None
		self.perfumes = None
		self.update(**kwargs)

	def update(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)

mfcsam = {	'children' : 3,
			'cats' : 7,
			'samoyeds' : 2,
			'pomeranians' : 3,
			'akitas' : 0,
			'vizslas' : 0,
			'goldfish' : 5,
			'trees' : 3,
			'cars' : 2,
			'perfumes' : 1}


with open('input') as f:
	for line in f:
		fail = False
		cand_data = {}
		_, nr, datta = line.split(' ', 2)
		datta = datta.split(',')
		for k, v in map(lambda x: x.split(':'), datta):
			cand_data[k.strip()] = int(v)

		candidate = Aunt(**cand_data)

		for k in candidate.__dict__:
			if candidate.__dict__[k] is None or candidate.__dict__[k] == mfcsam[k]:
				continue
			else:
				fail = True
				break
		if not fail:
			print nr[:-1]
			exit(0)
