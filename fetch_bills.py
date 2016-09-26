#!/bin/python
from lxml import html
from my_email import email
import datetime
import requests
import pdfkit

hydro_login = "https://www.wnhwebpresentment.com/app/capricorn?para=index"
session = requests.session()
placeholder = {
                'accessCode':'whmrtm@gmail.com',
                'password':'WHM9316rtm',
                'rememberMyAccountNumber':'Y'
                }
response = session.post(hydro_login, 
                data = placeholder,
                headers = dict(referer = hydro_login))

today = datetime.date.today()
month = "%02d" % today.month
to_day = "%02d" % today.day



price_url = "https://www.wnhwebpresentment.com/app/capricorn?para=usageComparison&inquiryType=hydro&fromYear=2016&fromMonth="+ month +"&fromDay=01&toYear=2016&toMonth="+ month +"&toDay=" + to_day
price_response = session.get(price_url, headers = dict(referer = price_url))
price_html = price_response.text

print(price_html)
#daily_consumption_url = "https://www.wnhwebpresentment.com/app/capricorn?para=smartMeterConsum"
#daily_response = session.get(daily_consumption_url, headers = dict(referer = daily_consumption_url))
#daily_html = daily_response.text

my_email = email()
my_email.set_default()
my_email.set_result("Hydro Price", price_html)
# my_email.send()
