import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url =  input("Enter-")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

#retrieve all the anchor tags
tags = soup('p')
for tag in tags:
    print(tag)