import json

def traverse(inp):
	if isinstance(inp, int):
		yield inp
	elif isinstance(inp, dict):
		if not "red" in inp.values():
			for value in inp.values():
				for subvalue in traverse(value):
					yield subvalue
	elif isinstance(inp, list):
		for value in inp:
			for subvalue in traverse(value):
				yield subvalue


inp = json.loads(open('input', 'r').read())
print sum(traverse(inp))
