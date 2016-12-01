adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
lights = {}
corners = [(0,0), (0,99), (99,99), (99,0)]

with open('input') as f:
	for y, line in enumerate(f):
		for x, c in enumerate(line):
			lights[(x,y)] = c == '#'
	for x, y in corners:
		lights[(x,y)] = True
			
def adjacent_cells(x,y, grid):
	for ax, ay in adjacency:
		if 0 <= (x + ax) < 100 and 0 <= (y + ay) < 100:
			yield grid[x + ax, y + ay]

def step(in_state, steps_left):
	if not steps_left:
		return in_state
	new_state = in_state.copy()
	for y in range(100):
		for x in range(100):
			if (x,y) in corners:
				continue

			# Readability
			light_on = in_state[(x,y)] 
			lighted_neighbours = sum(adjacent_cells(x,y, in_state))

			if light_on:
				if lighted_neighbours not in [2,3]:
					new_state[(x,y)] = False
			else:
				if lighted_neighbours == 3:
					new_state[(x,y)] = True
	return step(new_state, steps_left - 1)

print sum(step(lights, 100).values())	
