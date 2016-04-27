

import requests
import random



def test_openurl(baseurl):
	r = requests.get(baseurl+'q=London,uk&appid=6ceac7294286140698fbb9c2809b3a60')
	a =(r.status_code == requests.codes.ok)
	return a

def to_check_for_weather(baseurl):
	r = requests.get(baseurl+'q=London,uk&appid=6ceac7294286140698fbb9c2809b3a60')
	data = r.text
	return data

def to_generate_different_urls(baseurl,urlparam):
	r = requests.get(baseurl+urlparam+'&appid=6ceac7294286140698fbb9c2809b3a60')
	b =(r.status_code == requests.codes.ok)
	return b



	

