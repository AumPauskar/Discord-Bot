from bs4 import BeautifulSoup
import requests
import html5lib
import csv

def f1_webscraper():
	file = open('temp.txt', 'w')
	url = "https://www.formula1.com/en/results.html/2022/drivers.html"
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')
	html = soup.prettify
	article = soup.find('article')
	val = article.find('tbody')
	file.write(val.text)
	file.close()

	file = open('temp.txt', 'r')
	buffer = (file.read()).split('\n')
	cursor = 0
	output = []
	for i in range(21):
		output_sub = []
		cursor += 3
		output_sub.append(buffer[cursor]); cursor += 5
		output_sub.append(buffer[cursor]); cursor += 3
		output_sub.append(buffer[cursor]); cursor += 2
		output_sub.append(buffer[cursor]); cursor += 2
		output_sub.append(buffer[cursor]); cursor += 2
		output.append(output_sub)


	# field names 
	fields = ['Position', 'Name', 'Nationality', 'Team', 'Points'] 
		
	# writing to csv file 
	with open('f1_standings.csv', 'w') as csvfile: 
		# creating a csv writer object 
		csvwriter = csv.writer(csvfile) 
			
		# writing the fields 
		csvwriter.writerow(fields) 
			
		# writing the data rows 
		csvwriter.writerows(output)

	return 'Data return in CSV file'