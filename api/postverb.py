import pytest
import requests


#baseurl= 'http://api.openweathermap.org/data/2.5/weather?'
#apikey = '6ceac7294286140698fbb9c2809b3a60'

#print (baseurl)

def test_openurl( baseurl):
	r = requests.get(baseurl)
	assert r.status_code == 401

data=data
def test_to_check_for_weather(baseurl,data):
	print (baseurl+'q=London,uk&appid=6ceac7294286140698fbb9c2809b3a60')
	r = requests.get(baseurl+'q=London,uk&appid=6ceac7294286140698fbb9c2809b3a60')
	#print (r.text)
	data= r.text
	print (data)
	return data

print (data)



