from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.better.org.uk/leisure-centre/belfast")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>

print(title)