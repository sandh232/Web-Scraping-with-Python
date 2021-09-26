# Web Scraping 
# Using libraries like beautiful soup and requests
import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YU_TVbhKjIW")

#Beautifulsoup object, makes web scraping of page easy, gives you nice structure, classes, paragraph tags, html tags

soup = BeautifulSoup(page.content, 'html.parser')
week =soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")

#print(items[0])

#for i in range(len(items)):
 #print(items[i].find(class_='period-name').get_text())
 #print(items[i].find(class_='short-desc').get_text())
 #print(items[i].find(class_='temp').get_text())
 #print()

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_desc)
#print(temperatures)

weather_stuff = pd.DataFrame(
  {
  'Period':period_names,
  'Short description': short_desc,
  'Temperature': temperatures
  })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')