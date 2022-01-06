from typing import List, Any

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:/Users/Student/Desktop/CIS CLASS/MOD 3/CIS 403/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

# extract the data from the parst source and put it in the list
for a in soup.findAll(attrs='blog-card__content-wrapper') :
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='blog-card__user-info__wrapper') :
    author = b.find('p')
    if author not in other_results:
        other_results.append(author.text)

# create a variable that will create a table
df = pd.DataFrame({'Titles': results, 'Authors': other_results})
df.to_csv("names.csv", index=False, encoding='utf-8')
