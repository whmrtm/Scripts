#!/usr/bin/python

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

        def get_info(self):
                print("Please input the email address you want to send to: ")
                self._to = input()
                print("Subject: ")
                self._subject = input()
                print("Content: ")
                self._content = input()


my_email = email()
my_email.send()

