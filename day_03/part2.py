from collections import Counter

lines = open("input.txt").read().splitlines()
sacks = []
for i in range(0, len(lines), 3):
     sacks.append(lines[i:i+3])
commonChars = []
for sack in sacks:
    dict1 = Counter(sack[0])
    dict2 = Counter(sack[1])
    dict3 = Counter(sack[2])
    commonDict = dict1 & dict2 & dict3

    commonChars.append(list(commonDict.elements()))
priority = 0 
for char in commonChars:
    if (char[0].isupper() == True):
        priority += ord(char[0]) - 38
    else:
        priority += ord(char[0]) - 96
print(priority)