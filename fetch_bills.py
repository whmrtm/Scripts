#!/bin/python
from lxml import html
from my_email import email
import requests

rogers_login_url = "https://www.rogers.com/web/totes/#signin"
session = requests.session()
placeholder = {
                'USER':'whmrtm@gmail.com',
                'password':'whm9316rtm'
                }
response = session.post(rogers_login_url, 
                data = placeholder,
                headers = dict(referer = rogers_login_url))



test = "https://www.rogers.com/web/totes/#/accountOverview"
t = session.get(test, headers = dict(referer=test))
print(t.history)
print(t.status_code)
