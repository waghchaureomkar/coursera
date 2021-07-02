import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

tags = soup('count')
sum = None
count = 0
for tag in tags:
    x = tag.contents[0]
    y =  int(x)
    count = count + 1
    if sum == None:
        sum = y
        continue
    sum = sum + y
print (count)
print (sum)



  