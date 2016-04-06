import pytest
import requests
import conftest

r= requests.get(conftest.baseurl + 'weather?q=London,uk&appid='+ conftest.apikey)
data = r.json()
print(data)

def test_hello():
    print ('hello world')
    print (data)

print(test_hello())