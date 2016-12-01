from itertools import groupby

inp ="1113122113"

def do_own_group(inp):
	outp = ""
	current = inp[0]
	count = 1
	for c in inp[1:]:
		if c != current:
			outp += str(count) + current 
			current = c
			count = 1
		else:
			count += 1
	outp += str(count) + current
	return outp

def do_group(inp):
	return ''.join([str(len(list(v))) + k for k,v in groupby(inp)])

for i in range(40):
	inp = do_own_group(inp)
print "10.1", len(inp)

for i in range(10):
	inp = do_own_group(inp)
print "10.2", len(inp)
