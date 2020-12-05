import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://programmingwithmosh.com/courses")
soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())
courses = soup.find("div",{"class":"row course-list list"}).find_all("div",{"class":"course-listing-title"})
print(courses[0].get_text())

classes = [cls.get_text().strip() for cls in courses]
print(classes)
count = 1
for i in classes:
    print( str(count) + " : " + i)
    count += 1

