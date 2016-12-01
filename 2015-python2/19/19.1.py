translations = set()
answers = set()

def find_indices(substr, instr, currindex = 0, indices = []):
	index = instr.find(substr, currindex)
	if index == -1:
		return indices
	else:
		return find_indices(substr, instr, index + 1, indices + [index])

print find_indices("a","abcdaaa")
print find_indices("o","oooooo")

with open('input') as f:
	for line in f:
		if len(line.split(' => ')) == 2:
			translations.add(tuple(line.strip().split(' => ')))
		else:
			string = line.strip()
j = 0
for k, v in translations:
	for index in find_indices(k, string):
		answers.add(string[:index] + v + string[index+1:])
		j+=1

