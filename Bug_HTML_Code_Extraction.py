## Using the BeautifulSoup package to extract the webpage HTML code.

import requests
from bs4 import BeautifulSoup

...
url = "https://test.streamroot.io/candidates/test.html"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())
