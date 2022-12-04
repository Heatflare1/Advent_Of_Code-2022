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
	for rangemin, numb in enumerate(numbpairs):
		if (rangemin >= int(numb[0]) and rangemin <= int(numb[1])):
			overlaps += 1
		elif (rangemax >= int(numb[0]) and rangemax <= int(numb[1])):
			overlaps += 1
		elif (int(numb[0]) >= rangemin and int(numb[1]) <= rangemax):
			overlaps += 1
		rangemin = int(numb[0])
		rangemax = int(numb[1])
	rangemin = -1
	rangemax = -1
print(overlaps)