#!/bin/python
from lxml import html
from my_email import email
import datetime
import requests

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

dat://www.wnhwebpresentment.com/app/capricorn?para=smartMeterConsum&inquiryType=hydro
today = datetime.date.today()
month = "%2d" % today.month
to_day = "%2d" % today.day
daily_consumption_url = "https://www.wnhwebpresentment.com/app/capricorn?para=smartMeterConsum&inquiryType=hydro&frommYear=2016&fromMonth=" + month +"&fromDay=01&toYear=2016&toMonth=" + month + "&toDay=" + to_day
daily_response = session.get(daily_consumption_url, headers = dict(referer = daily_consumption_url))
daily_html = daily_response.text

#price_url = "https://www.wnhwebpresentment.com/app/capricorn?para=usageComparison&inquiryType=hydro"
#print(daily_response.text)
#price_response = session.get(price_url, headers = dict(referer = price_url))
#price_html = price_response.text


print(daily_html + price_html)
