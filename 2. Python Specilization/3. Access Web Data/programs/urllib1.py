import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('https://www.facebook.com/')
for line in fhand:
    print(line.decode().strip())
    

