import sys

class Node:
	def __init__(self, location):
		self.location = location
		self.adjacent = {}

	def visit(self):
		self.visited = True
		mini = sys.maxint
		togo = None
		for n, d in self.adjacent.items():
			if nodes[n].visited:
				continue
			else:
				if d < mini:
					mini = d
					togo = n
		if not togo:
			return 0
		return self.adjacent[togo] +  nodes[togo].visit()
		
	def reset(self):
		self.visited = False

nodes = {}
with open('input') as f:
	for line in f:
		first, _, second, _, distance = line.split()
		if first not in nodes.keys():
			nodes[first] = Node(first)
		if second not in nodes.keys():
			nodes[second] = Node(second)
		nodes[first].adjacent[second] = int(distance)
		nodes[second].adjacent[first] = int(distance)

	candidates = []
	for k in nodes.keys():
		map(lambda x: x.reset(), nodes.values())
		candidates.append(nodes[k].visit())
	print min(candidates)
