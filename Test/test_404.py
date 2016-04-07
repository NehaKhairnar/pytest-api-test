
import base
import pytest
import requests
@pytest.mark.parametrize("input,expected", [
    ((base.baseurl + 'weather?q=London,uk&appid='+base.apikey), 'London')
])

def test_eval(input, expected):
    r = requests.get(input)
    data= r.text
    assert r.text == expected
    assert r.status_code==200
    assert r.headers['Content-Type']=='text/plain'
    return data

print (data)