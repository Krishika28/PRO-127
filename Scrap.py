from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("./chromeDriver/chromedriver")
browser.get(url)
time.sleep(15)

def scraper():

    headers = ["Name","Distance","Mass","Radius"]

    planet_data = []

    soup = BeautifulSoup(browser.page_source, "html.parser" )    
    star_table = soup.find("table")
    rows = star_table.find_all("tr")

    for i in rows:
        td = i.find_all("td")
        planet_data.append([j.text.rstrip() for j in td ])
    
    print(planet_data[0:5])
    name = []
    distance = []
    mass = []
    radius = []

    for i in range(1,len(planet_data)):
        name.append(planet_data[i][1])
        distance.append(planet_data[i][3])
        mass.append(planet_data[i][5])
        radius.append(planet_data[i][6])
  
    df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns = headers)
    df.to_csv("stars.csv")

scraper()