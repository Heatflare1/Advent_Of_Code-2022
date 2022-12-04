from collections import Counter

lines = open("input.txt").read().splitlines()
sacks = []
for line in lines:
    sack = [line[:len(line)//2], line[len(line)//2:]]
    sacks.append(sack)
commonChars = []
for sack in sacks:
    dict1 = Counter(sack[0])
    dict2 = Counter(sack[1])
    commonDict = dict1 & dict2

    commonChars.append(list(commonDict.elements()))
priority = 0 
for char in commonChars:
    if (char[0].isupper() == True):
        priority += ord(char[0]) - 38
    else:
        priority += ord(char[0]) - 96
print(priority) 
