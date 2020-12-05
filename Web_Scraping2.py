import pandas as pd                                                #for data arranging we import pandas and it is optional
import requests                                                   #to get http request we import this module
from bs4 import BeautifulSoup                                     #this is for web scraping(extracting whatever data we want from the file)
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.X2XreGgzZPY")
soup = BeautifulSoup(page.content,"html.parser")                     #the first paramter page.content- is used to get the html in readable format and second one is "html.parser" is used to parse the html page,parsing means extracting the important data from a text like title ,tags,etc,..here soup object will form a tree like structure for ease of extracting data
print(soup.prettify())                                                #without this prettify method it will html without indentation which is worst to read ,so prettify() indents html page which looks well when reading
week = soup.find(id="seven-day-forecast-body")                      #in that soup object(which is a tree) we are extracting(find()) a id
#print(week)
items = week.find_all(class_="tombstone-container")
print(items[0])
print(items[0].find(class_="period-name").get_text())
print(items[0].find(class_="short-desc").get_text())
print(items[0].find(class_="temp").get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
print(period_names)
print(short_descriptions)
print(temperatures)

#using pandas for tabling the result data:
weather_stuff = pd.DataFrame(
    {
        'period':period_names,
        'short_descriptions':short_descriptions,
        'temperatures':temperatures,
    }
)
print(weather_stuff)
weather_stuff.to_csv('weather.csv')


