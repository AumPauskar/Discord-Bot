from bs4 import BeautifulSoup
import requests
import html5lib

def sendbtc():
	url = "https://www.google.com/search?q=bitcoin+price"
	source = requests.get(url)
	soup = BeautifulSoup(source.text, 'html.parser')
	html = soup.prettify()
	val = (soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).find("div", {"class": "BNeawe iBp4i AP7Wnd"})).text
	return val

def sendeth():
	url = "https://www.google.com/search?q=ethereum+price"
	source = requests.get(url)
	soup = BeautifulSoup(source.text, 'html.parser')
	html = soup.prettify()
	try:
		val = (soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).find("div", {"class": "BNeawe iBp4i AP7Wnd"})).text
	except:
		val = "Sorry for the inconvenience the price couldn't be found out"
	return val


def sendxmr():
	url = "https://www.google.com/search?q=monero+price"
	source = requests.get(url)
	soup = BeautifulSoup(source.text, 'html.parser')
	html = soup.prettify()
	val = (soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).find("div", {"class": "BNeawe iBp4i AP7Wnd"})).text
	return val

def senddoge():
	url = "https://www.google.com/search?q=dogecoin+price"
	source = requests.get(url)
	soup = BeautifulSoup(source.text, 'html.parser')
	html = soup.prettify()
	val = (soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).find("div", {"class": "BNeawe iBp4i AP7Wnd"})).text
	return val
