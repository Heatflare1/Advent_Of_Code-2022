# oh no..
lines = open("input").read().splitlines()
rules = dict.fromkeys(['A', 'X'], 1)
rules.update(dict.fromkeys(['B', 'Y'], 2))
rules.update(dict.fromkeys(['C', 'Z'], 3))
games = [x.split() for x in lines]
tourney = []
for game in games:
	my_list = [rules.get(play) for play in game]
	tourney.append(my_list)
points = 0
for game in tourney:
	if (game[1] == 1):
		if (game[0] == 1):
			points += 3
		else:
			points += abs(game[0] - 1)
	if (game[1] == 2):
		points += 3
		points += game[0]
	if (game[1] == 3):
		points += 6
		if (game[0] == 3):
			points += 1
		else:
			points += abs(game[0] + 1)
print(points)