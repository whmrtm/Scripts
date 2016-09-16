
import urllib.request
import urllib.response
import urllib.parse
import smtplib
from email.mime.text import MIMEText
import re
import time

class fetch_from_bulletin:
  def __init__(self, url, to, sender, passwd, interval):
    self._myUrl = url
    self.User_agent = "Mozilla/4.0(compatible;MSIR 5.5;Windows NT)"
    self._headers = {"User-Agent":self.User_agent}
    self._sender = sender
    self._passwd = passwd
    self._to = to
    self._interval = interval
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
 
  def send_email(self, msg):
    body = MIMEText(msg,'html')
    body['From'] = self._sender
    body['To'] = self._to
    body['Subject'] = "Daily Bulletin of UW"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    try:
      server.login(self._sender, self._passwd)
      print("Login is successful")
    except:
      print('Login error!')
    try:
      server.sendmail(self._sender, self._to, body.as_string())
      print("Mail successfully sent!")
    except:
      print('Error! Mail sent failure!')
    server.close()
  def start(self):
    while(1):
      msg = self.get_events()
      print(msg)
      self.send_email(msg)
      time.sleep(self._interval)



url = "https://uwaterloo.ca/daily-bulletin"
to = "whmrtm@gmail.com"
sender = "whmowen@gmail.com"
passwd = "whm9316rtm"
interval = 3600*24

fetch = fetch_from_bulletin(url, to, sender, passwd, interval)
fetch.start()
