import pytest


@pytest.fixture(scope="module") #fixture for generating baseurl 
def baseurl():
	url= 'http://api.openweathermap.org/data/2.5/weather?'
	return url

@pytest.fixture( scope="module", params=['q=London,uk','lat=35&lon=139','id=2172797'])
def urlparam(request):
    return request.param


