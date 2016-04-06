import pytest
import requests

r= requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=8cdf78ace3f304f515bccc14d2206017')
data = r.json()
print(data)