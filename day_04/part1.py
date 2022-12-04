lines = open("input").read().splitlines()
elves = [x.split(',')for x in lines]
ids = []
for numbs in elves:
	pairs = [pair.split('-') for pair in numbs]
	ids.append(pairs)
overlaps = 0
rangemin = -1
rangemax = -1
for numbpairs in ids:
	for numb in numbpairs:
		if (rangemin >= int(numb[0]) and rangemax <= int(numb[1])):
			overlaps += 1
		elif (rangemin <= int(numb[0]) and rangemax >= int(numb[1])):
			overlaps += 1
		rangemin = int(numb[0])
		rangemax = int(numb[1])
	rangemin = -1
	rangemax = -1
print(overlaps)