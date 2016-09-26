#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText




class email:
        def __init__(self):
                self._from = ""
                self._passwd = ""
                self._to = ""
                self._subject = ""
                self._content = ""
        def send(self):
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

        def set_from(self, user):
                self._from = user
        def set_to(self, to):
                self._to = to
        def set_passwd(self, content):
                self._passwd = passwd
        def set_subject(self, subject):
                self._subject = subject
        def set_content(self, content):
                self._content = content
        def set_result(self, subject, content):
                self.set_subject(subject)
                self.set_content(content)
        def set_default(self):
                self._from = "whmrtm@gmail.com"
                self._to = "whmrtm@gmail.com"
                self._passwd = "xxxx"
        

