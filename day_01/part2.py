
# codam wayy..
my_list = []
numb = 0
i = open('example', 'r')
f_lines = i.read()
better = f_lines.split("\n\n")
for string in better:
	my_list.append(string.split())
for lst in my_list: 
	for i in range(len(lst)):
		lst[i] = int(lst[i])
added_list = []
for lst in my_list:
	for number in lst:
		numb += number
	added_list.append(numb)	
	numb = 0
added_list.sort(reverse=True)
numb = added_list[0] + added_list[1] + added_list[2]
print(numb)