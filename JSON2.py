import json
import urllib.request,urllib.parse
page = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_595924.json").read()
lds = json.loads(page)
print(lds)
comments = lds["comments"]
print(comments)
lst = []
count =0
for comment in  comments:
    num = int(comment["count"])
    count += 1
    lst.append(num)
print(lst)
print(count)
print(sum(lst))