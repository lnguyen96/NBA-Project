import csv
import bs4
import sys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

players = {}
ids = []

with open('playerIDs.csv') as DataFile:
	csvReader = csv.reader(DataFile)
	next(DataFile)
	for row in csvReader:
		#print('Name:',row[0])
		#print('ID:',row[1])
		players[row[1]] = row[0]
		ids.append(row[1])

#print(players)
#print(ids)
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

print(ids[0])

myUrl = 'https://stats.nba.com/player/' + ids[0] + '/boxscores-traditional/'

print(myUrl)

driver.get(myUrl)

'''try:
	select = select()
except:
	continue
'''
driver.close()