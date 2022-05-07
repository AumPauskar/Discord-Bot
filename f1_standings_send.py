import csv

def f1_send():
	with open('f1_standings.csv', 'r') as file:

		buffer = '```'
		data = []
		csvfile = csv.reader(file)
		for lines in csvfile:
			data.append(lines)

	for i in range(1, 10):
		if data[i][3] == 'Ferrari':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'FER' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Red Bull Racing RBPT':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'RBR' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Mercedes':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'MER' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'McLaren Mercedes':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'MCL' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Alfa Romeo Ferrari':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'ALR' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Alpine Renault':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'ALP' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Haas Ferrari':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'HAA' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'AlphaTauri RBPT':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'ALT' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Aston Martin Aramco Mercedes':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'AMR' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Williams Mercedes':
			buffer += (data[i][0] + ' \t' + data[i][1] + '\t' + data[i][2] + '\t' + 'WIL' + '\t' + data[i][4]) + '\n'

	for i in range(10, 22):
		if data[i][3] == 'Ferrari':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'FER' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Red Bull Racing RBPT':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'RBR' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Mercedes':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'MER' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'McLaren Mercedes':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'MCL' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Alfa Romeo Ferrari':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'ALR' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Alpine Renault':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'ALP' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Haas Ferrari':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'HAA' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'AlphaTauri RBPT':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'ALT' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Aston Martin Aramco Mercedes':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'AMR' + '\t' + data[i][4]) + '\n'
		elif data[i][3] == 'Williams Mercedes':
			buffer += (data[i][0] + '\t' + data[i][1] + '\t' + data[i][2] + '\t' + 'WIL' + '\t' + data[i][4]) + '\n'

	buffer += '```'
	return buffer