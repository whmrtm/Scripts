#!/bin/python3


import re
import urllib.request
import sys


response = urllib.request.urlopen('http://amazon.ca/')
my_html = response.read()

print(my_html)
