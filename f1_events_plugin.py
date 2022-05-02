# importing all the modules
import csv
import time

def f1_schedule():
	# bases
	file = 'f1_events_data.csv'
	rows = 0
	round = 1
	total_rows = 2
	buffer = []
	msg = ''

	# opening th file and storing in a variable
	with open(file, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			rows += 1
			# tmp = str(row)
			buffer.append(row)

	today_mo = time.strftime('%m')
	today_da = time.strftime('%d')

	for i in range(2):
		# extracting dates to compare
		rw_st_mo = buffer[round][0][3]+buffer[round][0][4]
		rw_st_da = buffer[round][0][6]+buffer[round][0][7]
		rw_en_mo = buffer[round][0][12]+buffer[round][0][13]
		rw_en_da = buffer[round][0][15]+buffer[round][0][16]
		# the race event finder
		# dates of all events stored here
		event1_date = buffer[round][3][6]+buffer[round][3][7]+'/'+buffer[round][3][3]+buffer[round][3][4]+'/'+buffer[round][3][0]+buffer[round][3][1]
		event2_date = buffer[round][4][6]+buffer[round][4][7]+'/'+buffer[round][4][3]+buffer[round][4][4]+'/'+buffer[round][4][0]+buffer[round][4][1]
		event3_date = buffer[round][3][6]+buffer[round][5][7]+'/'+buffer[round][5][3]+buffer[round][5][4]+'/'+buffer[round][5][0]+buffer[round][5][1]
		event4_date = buffer[round][3][6]+buffer[round][6][7]+'/'+buffer[round][6][3]+buffer[round][6][4]+'/'+buffer[round][6][0]+buffer[round][6][1]
		event5_date = buffer[round][3][6]+buffer[round][7][7]+'/'+buffer[round][7][3]+buffer[round][7][4]+'/'+buffer[round][7][0]+buffer[round][7][1]

		if (rw_st_mo == today_mo) and (today_da < rw_st_da):
			break
		else:
			round += 1

	# timings of all events stored here (24hrs)
	event1_time = buffer[round][3][9]+buffer[round][3][10]+':'+buffer[round][3][12]+buffer[round][3][13]
	event2_time = buffer[round][4][9]+buffer[round][4][10]+':'+buffer[round][4][12]+buffer[round][4][13]
	event3_time = buffer[round][5][9]+buffer[round][5][10]+':'+buffer[round][5][12]+buffer[round][5][13]
	event4_time = buffer[round][6][9]+buffer[round][6][10]+':'+buffer[round][6][12]+buffer[round][6][13]
	event5_time = buffer[round][7][9]+buffer[round][7][10]+':'+buffer[round][7][12]+buffer[round][7][13]
	event_name = buffer[round][1]
	msg += 'The event is located in ' + str(event_name) + '\n'
	if buffer[round][2][0] == 'n':
		msg += 'It has a normal qualifying format.\n'
		msg += 'Free Practice 1: ' + str(event1_date) + ' at time: ' + str(event1_time) + '\n'
		msg += 'Free Practice 2: ' + str(event2_date) + ' at time: ' + str(event2_time) + '\n'
		msg += 'Free Practice 3: ' + str(event3_date) + ' at time: ' + str(event3_time) + '\n'
		msg += 'Qualifying: ' + str(event4_date) + ' at time: ' + str(event4_time) + '\n'
		msg += 'Race: ' + str(event5_date) + ' at time: ' + str(event5_time) + '\n'

	elif buffer[round][2][0] == 's':
		msg += 'The event inculdes a sprint qualifying format.\n'
		msg += 'Free Practice 1: ' + str(event1_date) + ' at time: ' + str(event1_time) + '\n'
		msg += 'Qualifying: ', str(event2_date) + ' at time: ' + str(event2_time) + '\n'
		msg += 'Free Practice 2: ' + str(event3_date) + ' at time: ' + str(event3_time) + '\n'
		msg += 'Sprint: ' + str(event4_date) + ' at time: ' + str(event4_time) + '\n'
		msg += 'Race: ' + str(event5_date) + ' at time: ' + str(event5_time) + '\n'

	return msg