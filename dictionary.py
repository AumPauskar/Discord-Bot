def Word():
	import random
	file = open('command-texts/popular.txt', 'r')
	data = file.read()
	data = data.split('\n')
	r = random.randint(0, len(data)-1)
	return data[r]

