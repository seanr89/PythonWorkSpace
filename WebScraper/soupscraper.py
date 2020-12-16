from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.better.org.uk/leisure-centre/belfast")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>

print(title)

centres_list = soup.find_all('article', class_ = 'venue-result-panel')

#print(type(centres_list))
#print(len(centres_list))

first_record = centres_list[0]
#print(first_record)
print(first_record.h1.a.text)

addressdiv = first_record.find('div', class_ = 'venue-result-panel__address')
print(addressdiv.text)