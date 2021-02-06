# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:15:12 2021

@author: Henrique Wills
"""

import requests
from bs4 import BeautifulSoup

...
url = "https://test.streamroot.io/candidates/test.html"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())