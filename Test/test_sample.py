
import pytest
import requests
from api.main import *



def test_if_url_is_valid(baseurl): #checks if url is reponding correct 200 status
	b= test_openurl(baseurl)
	assert b == True

def test_api_reponse_by_country(baseurl): #verifies if Country is present in api reponse stored in variable a
	a=to_check_for_weather(baseurl)
	assert 'London' in a


def test_a(baseurl,urlparam): # checks for muitple urls

	status= to_generate_different_urls(baseurl,urlparam)
	print (status)
	assert status == True
	if True:
		print ("Hurray! This url is a valid url",urlparam)
	else:
		print ("Oops! There has been a issue",urlparam)

#@pytest.mark.parametrize("x", [0, 1])
def to_check_if_response_generated(baseurl,urlparam):
	data= to_generate_different_urls(baseurl,urlparam)
	print(data)


