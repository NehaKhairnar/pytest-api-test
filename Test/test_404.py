import pytest
import requests
import conftest

r= requests.get(conftest.baseurl + 'weather?q=London,uk&appid='+ conftest.apikey)
data = r.json()
print(data)

assert data == data