#!/bin/python3

import requests
import re
import urllib.request
import sys
import json
from my_email import email


my_url = "https://learn.uwaterloo.ca"

session_requests = requests.session()
# result = session_requests.get(my_url)
payload = json.dumps({'username':'h422wang', 'password':'WLD9342&zry', 'lt':'e3s1'})
result = session_requests.post(my_url, data = payload, headers = dict(referer = my_url)
                )
print(result.status_code)
print(result.history)
print(result.text)



# Send the email through my email class

my_email = email()
my_email.set_default()
my_email.set_to("whmowen@gmail.com")
my_email.set_subject("Fetch torrent lists")


# my_email.send()
