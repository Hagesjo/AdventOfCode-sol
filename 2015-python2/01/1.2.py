with open('input') as f:
	inp = f.read()

floor = 0
for i in enumerate(inp):
	if i[1] == '(':
		floor += 1
	elif i[1] == ')':
		floor -= 1	
	if floor == -1:
		print i[0] + 1
		break
