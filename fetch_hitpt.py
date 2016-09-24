#!/bin/python3

import requests
import re
from my_email import email
from lxml import html
# Login

login_url = "https://pt.hit.edu.cn/takelogin.php"
session_requests = requests.session()
payload = {
            "username":"whmrtn@126.com",
            "password":"whm9316rtm"
                }
result = session_requests.post(login_url, data = payload, headers = dict(referer = login_url))

# Access torrent page
torrent_url = "https://pt.hit.edu.cn/torrents.php"
response = session_requests.get(torrent_url, headers = dict(referer = torrent_url))
torrent_html = response.text

# Grep the necessary information (torrent list)
tree = html.fromstring(torrent_html)
torrentname = tree.findall(".//table[@class='torrentname']/")
torrent_name_list = []
for table in torrentname:
        for element in table.iter("a"):
                if 'title' in element.attrib:
                        name = element.attrib['title']
                        torrent_name_list.append(name)

print(torrent_name_list)

# Send the email through my email class

my_email = email()
my_email.set_default()
my_email.set_to("whmowen@gmail.com")
my_email.set_subject("Fetch torrent lists")
my_email.set_content(str(torrent_name_list))

# my_email.send()
