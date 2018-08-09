import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://stats.nba.com/player/203518/'

uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each team table
containers = page_soup.findAll('script')

#print(containers)
print(containers[1])
