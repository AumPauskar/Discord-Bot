def SendMessage():
	import requests
	import os
	import time
	import csv

	city_name = 'Belgaum'
	api_key = os.environ.get('W_API')
	api_link = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
	order = requests.get(api_link)
	data = order.json()
	kc = 273.15 


	if data['coord'] == 404:
		print("City not found on the database")
	else:
		print("City found on the database")
		weather_description = data['weather'][0]['description']
		temp = (data['main']['temp'])-kc
		humidity = data['main']['humidity']

		values = 'Currently weather in Belgaum is:' + str(round(temp)) +' C' + ', ' + weather_description + ', ' + 'Humidity levels at: ' +str(humidity) +'%'

	return values


print(SendMessage())