import xml.etree.ElementTree as ET
import urllib.request,urllib.parse
page = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_595923.xml").read()
print(page)
lst = []
count =0
tags = ET.fromstring(page)
comments = tags.findall("comments/comment")
print(len(comments))
for comment in comments:
    comm_count = int(comment.find("count").text)
    lst.append(comm_count)
    count += 1
print("count:",count)
print(sum(lst))




