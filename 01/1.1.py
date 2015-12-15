with open('input') as f:
	inp = f.read()
floor = 0
for i in inp:
	if i == '(':
		floor += 1
	elif i == ')':
		floor -= 1	
print floor
