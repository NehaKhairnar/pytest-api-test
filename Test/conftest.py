# content of ./conftest.py
import pytest


aseurl = api.openweathermap.org/
apikey = 6ceac7294286140698fbb9c2809b3a60


@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com")

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0 # for demo purposes