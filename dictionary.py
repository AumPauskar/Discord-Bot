import imp


def Word():
	import random
	file = open('command-texts/popular.txt', 'r')
	data = file.read()
	data = data.split('\n')
	r = random.randint(0, len(data)-1)
	return data[r]

def Sentence():
	import random
	file = open('command-texts/popular.txt', 'r')
	data = file.read()
	data = data.split('\n')
	sentence = ''
	l = random.randint(4, 20)
	for a in range(l):
		r = random.randint(0, len(data)-1)
		sentence += data[r]
		sentence += ' '
	return sentence

def LongSentence():
	import random
	file = open('command-texts/popular.txt', 'r')
	data = file.read()
	data = data.split('\n')
	sentence = ''
	l = random.randint(21, 100)
	for a in range(l):
		r = random.randint(0, len(data)-1)
		sentence += data[r]
		sentence += ' '
	return sentence