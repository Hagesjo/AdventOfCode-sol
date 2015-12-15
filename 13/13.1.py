import operator
from itertools import permutations

class Person:
	def __init__(self):
		self.others = {}

	def add_preference(self, other, value):
		self.others[other] = value

signs = {'gain' : operator.pos, 'lose' : operator.neg}

with open('input') as f:
	people = {}
	for line in f:
		person, _, sign, value, _, _, _, _, _, _, other = line[:-2].split() #  avoid period
		if not person in people:
			people[person] = Person()
		people[person].add_preference(other, signs[sign](int(value)))

max_happiness = 0

for order in permutations(people):
	current_happiness = 0
	for index, person in enumerate(order):
		current_happiness += people[person].others[order[(index+1) % len(order)]]
		current_happiness += people[person].others[order[(index-1) % len(order)]]
	max_happiness = max(max_happiness, current_happiness)
print max_happiness
