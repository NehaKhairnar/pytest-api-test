import pytest
import requests
import base

r= requests.get(base.baseurl + 'weather?q=London,uk&appid='+base.apikey)
data = r.json()
print(data)