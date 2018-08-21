from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as soup

# hides chrome browser opening
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://stats.nba.com/players/list/')

# set up csv file
filename = 'playerIDs.csv'
f = open(filename, 'w')
headers = 'Player Name, Player ID\n'
f.write(headers)

# opens connection
links = driver.find_elements_by_class_name('players-list__name')

# parses strings for player ids and player names
for link in links:
	pid = link.find_element_by_tag_name('a')
	pid_container = pid.get_attribute('href')
	player_name = pid.text
	player_name = player_name.split(',')
	if len(player_name) == 2:
		player_name = player_name[1] + ' ' + player_name[0]
		player_name = player_name.lstrip(' ')
	else:
		player_name = player_name[0]
		player_name = player_name.lstrip(' ')
	player_id = pid_container.split('/')
	player_id = player_id[4]
	f.write(player_name + ',' + player_id + '\n')

f.close()

driver.close()
