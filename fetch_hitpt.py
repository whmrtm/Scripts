#!/bin/python3

import requests
import re
import urllib.request
import sys
import json
from my_email import email


my_url = "https://pt.hit.edu.cn/login.php?returnto=torrents.php"

session_requests = requests.session()
# result = session_requests.get(my_url)
payload = json.dumps({'username':'whmrtn@126.com', 'password':'whm9316rtm'})
result = session_requests.post(my_url, data = payload, headers = dict(referer = my_url)
                )
print(result.status_code)
print(result.history)
print(result.text)

torrent_url = "https://pt.hit.edu.cn/torrents.php"
torrent_response = session_requests.get(torrent_url, headers = dict(referer = torrent_url), allow_redirects = True)


# Send the email through my email class

my_email = email()
my_email.set_default()
my_email.set_to("whmowen@gmail.com")
my_email.set_subject("Fetch torrent lists")
my_email.set_content(torrent_response.text)


# my_email.send()
