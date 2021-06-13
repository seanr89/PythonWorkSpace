from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.better.org.uk/leisure-centre/belfast")
#page = requests.get("https://www.better.org.uk/leisure-centre/cardiff")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>

print(title)

centres_list = soup.find_all('article', class_ = 'venue-result-panel')

# Extract data from individual container
for container in centres_list:
    #print(container.h1.a.text)
    addressdiv = container.find('div', class_ = 'venue-result-panel__address')
    print(addressdiv)

    contactdiv = container.find('div', class_ = 'venue-result-panel__contact')
    print(contactdiv)

    itemsdiv = container.find('div', class_ = 'venue-result-panel__items')
    print(itemsdiv)
