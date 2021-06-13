from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.better.org.uk/leisure-centre/belfast"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#https://realpython.com/beautiful-soup-web-scraper-python/

##print(soup.get_text())
print(soup.title)

articles = soup.find_all("article")
##print(articles)
for art in articles:
    #print(art, end='\n'*2)
    ##print("-----------------------------------------")
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = art.find('h2', class_='venue-result-panel__title')
    company_elem = art.find('div', class_='venue-result-panel__address')
    if title_elem is None:
        continue
    if None in (title_elem):
        continue
    print(title_elem.text)