# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = (1,2,3,4,5,6,7)
url = None
for x in count:
    if url == None:
        url = input('Enter url - ')
    else:
        url = y
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    
    tags = soup('a')
    p = 0
    for tag in tags:
        if p == 0:
            p = 1
            continue
        p = p + 1
        if p == 18:
            y = tag.get('href', None)
            print(y)
