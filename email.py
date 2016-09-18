#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText



user = "whmrtm@gmail.com"
passwd = "whm9316rtm"


class email:
        def __init__(self):
                self._from = "whmrtm@gmail.com"
                self._passwd = "whm9316rtm"
                self._to = ""
                self._subject = ""
                self._content = ""
        def send(self):
                self.get_info()
                body = MIMEText(self._content, 'html')
                body['From'] = self._from
                body['To'] = self._to
                body['Subject'] = self._subject
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                try:
                        server.login(self._from, self._passwd)
                        print("Login successful")
                except:
                        print("Login error!")

                try:
                        server.sendmail(self._from, self._to, body.as_string())
                        print("Mail sent!")
                except:
                        print("Mail sent error!")
                server.close()

        def get_info(self):
                print("Please input the email address you want to send to: ")
                self._to = input()
                print("Subject: ")
                self._subject = input()
                print("Content: ")
                self._content = input()


my_email = email()
my_email.send()

