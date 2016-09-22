#!/bin/python3

import requests
import re
import urllib.request
import sys
import json
from my_email import email


my_url = "https://pt.hit.edu.cn/takelogin.php"

session_requests = requests.session()
# result = session_requests.get(my_url)
payload = {
    "username":"whmrtn@126.com", 
    "password":"whm9316rtm",
    "logout":"yes",
    "securelogin":"no"}
result = session_requests.post(my_url, data = payload)

torrent_url = "https://pt.hit.edu.cn/torrents.php"
torrent_response = session_requests.get(torrent_url)

# Send the email through my email class

my_email = email()
my_email.set_default()
my_email.set_to("whmrtm@gmail.com")
my_email.set_subject("Fetch torrent lists")
my_email.set_content("response")

# my_email.send()
