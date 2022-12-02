
lines = open("input").read().splitlines()
my_dict = dict.fromkeys(['A', 'X'], 1)
my_dict.update(dict.fromkeys(['B', 'Y'], 2))
my_dict.update(dict.fromkeys(['C', 'Z'], 3))
games = [x.split() for x in lines]
tourney = []
for game in games:
	my_list = [my_dict.get(play) for play in game]
	tourney.append(my_list)
points = 0
for game in tourney:
	points += game[1]
	numb = game[1] - game[0]
	if (numb == 0):
		points += 3
	if (numb == 1 or game[1] == 1 and game[0] == 3):
		points += 6
print(points)
#Opponent
# A = Rock
# B = Paper
# C = Scissors

#Me
# X = 1p-Rock
# Y = 2p-Paper
# Z = 3p-Scissors

# Win = 6p
# Draw = 3p
# Lose = 0p

