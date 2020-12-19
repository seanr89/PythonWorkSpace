# import libraries
from bs4 import BeautifulSoup
import requests

# specify the url
quote_page = "http://www.bloomberg.com/quote/SPX:IND"
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
# query the website and return the html to the variable ‘page’
page = requests.get(quote_page, headers=headers)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html5lib')

title = soup.title.text
print(title)

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})
print(name_box)

# name = name_box.text # strip() is used to remove starting and trailing
# print(name)

# get the index price
# price_box = soup.find('div', attrs={'class':'price'})
# price = price_box.text
# print(price)