from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.better.org.uk/leisure-centre/belfast")
#page = requests.get("https://www.better.org.uk/leisure-centre/cardiff")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>

print(title)

centres_list = soup.find_all('article', class_ = 'venue-result-panel')

#print(type(centres_list))
#print(len(centres_list))

# Extract data from individual container
for container in centres_list:
    # container = centres_list[0]
    #print(first_record)
    print(container.h1.a.text)

    addressdiv = container.find('div', class_ = 'venue-result-panel__address')
    ##lines = addressdiv.findAll('br')
    #print(addressdiv.text)
    
    print(addressdiv)
    #content = str(addressdiv).replace("</br>", " ")
    #print(content)