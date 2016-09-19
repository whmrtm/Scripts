#!/bin/python

import urllib.request
import urllib.response
import urllib.parse
import re
from my_email import email



class fetch_from_bulletin:
  def __init__(self, url):
    self._myUrl = url
    self.User_agent = "Mozilla/4.0(compatible;MSIR 5.5;Windows NT)"
    self._headers = {"User-Agent":self.User_agent}
    self._html = ""

  def get_article(self):
    try:
      req = urllib.request.Request(self._myUrl)
      print('Obtain response from server')
    except:
      print('Error')
    response = urllib.request.urlopen(req)
    result = response.read()
    restlt = result.decode('utf8','ignore')
    return str(result)

  def get_events(self):
    html = self.get_article()
    p = re.compile('<div class="db_header_box_3">([\S\s.]+)</div>\S+\s+<div class="db_header_box_4">') 
    events = p.findall(html)
    event = events[0]
    event = re.sub('#', 'www.uwaterloo.ca/daily-bulletin#', event)
    return event

# fetch class set

url = "https://uwaterloo.ca/daily-bulletin"
fetch = fetch_from_bulletin(url)

# set email class and necessary information

my_email = email()
my_email.set_default()
my_email.set_subject("Daily bulletin of UW news")
my_email.set_to("whmowen@gmail.com")
my_email.set_content(fetch.get_events())


# send the email
my_email.send()





