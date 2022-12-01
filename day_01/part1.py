# codam way...
my_list = []
numb = 0
max = 0
i = open('input', 'r')
f_lines = i.read()
better = f_lines.split("\n\n")
for string in better:
	my_list.append(string.split())
for lst in my_list: 
	for i in range(len(lst)):
		lst[i] = int(lst[i])
for lst in my_list:
	for number in lst:
		numb += number
	if (numb > max):
		max = numb
	numb = 0
print(max)

# normal way..
i = open('example_i.txt', 'r').read().split("\n\n");
elves = [x.split() for x in i]
for i, lst in enumerate(elves):
	elves[i] = [int(x) for x in lst]
print(elves)
elves = [sum(x) for x in elves]
print(max(elves))

# little cursed..
i = open('example_i.txt', 'r').read().split("\n\n");
inventory = list()
for i, lst in enumerate([x.split() for x in i]):
	inventory.append(sum([int(x) for x in lst]))
print(max(inventory))

# WTF..
print(max(sum(map(int,l.split()))for l in open('e').read().split('\n\n')))