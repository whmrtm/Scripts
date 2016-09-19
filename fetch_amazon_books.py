#!/bin/python3

import urllib.request
import sys

response = urllib.request.urlopen('http://amazon.ca/')
html = response.read()

print(html)

