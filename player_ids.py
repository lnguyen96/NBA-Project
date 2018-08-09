import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

'''myUrl = 'https://stats.nba.com/players/list/'

uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
'''
#print(page_soup)

#for container in page_soup.findAll('a', href=True):
#	print('Found the URL:',container['href'])
#print(len(containers))

from string import ascii_lowercase
for c in ascii_lowercase:
	print(c)
