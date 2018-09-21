import csv
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

players = {}
ids = []

# put data from csv into dictionary
with open('playerIDs.csv') as DataFile:
	csvReader = csv.reader(DataFile)
	next(DataFile)
	for row in csvReader:
		#print('Name:',row[0])
		#print('ID:',row[1])
		players[row[1]] = row[0]
		ids.append(row[1])

options = webdriver.ChromeOptions()
#options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

for i in range(len(ids)):
	name = players.get(ids[i])
	filename = name + ' BoxScores.csv'
	f = open(filename, 'w')
	headers = 'Court Advantage, Opponent, W/L, MIN, PTS, FGM, FGA, FG%, 3PM, 3PA, 3P%, FTM, FTA, FT%, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PM\n'
	f.write(headers)

	myUrl = 'https://stats.nba.com/player/' + ids[i] + '/boxscores-traditional/'

	driver.get(myUrl)
	time.sleep(5)

	# used to gather all pages of table on webpage
	try:
		select = Select(driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[1]/div/div/select'))
		#select.select_by_value('All')
		select.select_by_visible_text('All')
		#time.sleep(5)
	except:
		pass

	# used to write all games currently displayed on webpage into csv file
	games = driver.find_elements_by_xpath('/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')
	for game in games:
		match = game.find_element_by_xpath('.//td[1]').text
		opp = match[-3:]
		if '@' in match:
			gametype = 'Away'
		else:
			gametype = 'Home'
		wl = game.find_element_by_xpath('.//td[2]').text
		minutes = game.find_element_by_xpath('.//td[3]').text
		pts = game.find_element_by_xpath('.//td[4]').text
		fgm = game.find_element_by_xpath('.//td[5]').text
		fga = game.find_element_by_xpath('.//td[6]').text
		fgper = game.find_element_by_xpath('.//td[7]').text
		threepm = game.find_element_by_xpath('.//td[8]').text
		threepa = game.find_element_by_xpath('.//td[9]').text
		threepper = game.find_element_by_xpath('.//td[10]').text
		ftm = game.find_element_by_xpath('.//td[11]').text
		fta = game.find_element_by_xpath('.//td[12]').text
		ftper = game.find_element_by_xpath('.//td[13]').text
		oreb = game.find_element_by_xpath('.//td[14]').text
		dreb = game.find_element_by_xpath('.//td[15]').text
		reb = game.find_element_by_xpath('.//td[16]').text
		ast = game.find_element_by_xpath('.//td[17]').text
		stl = game.find_element_by_xpath('.//td[18]').text
		blk = game.find_element_by_xpath('.//td[19]').text
		tov = game.find_element_by_xpath('.//td[20]').text
		pf = game.find_element_by_xpath('.//td[21]').text
		pm = game.find_element_by_xpath('.//td[22]').text
		f.write(gametype + ',' + opp + ',' + wl + ',' + minutes + ',' + pts + ',' + fgm + ',' + fga + ',' + fgper + ',' + threepm + ',' + threepa + ',' + threepper + ',' + ftm + ',' + fta + ',' + ftper + ',' + oreb + ',' + dreb + ',' + reb + ',' + ast + ',' + stl + ',' + blk + ',' + tov + ',' + pf + ',' + pm + '\n')
	f.close()
	#print(stl,blk,tov)

	#team1 = match[15:18]
	#team2 = match[-3:]
	#print(team1,team2)
	#print(gametype)
#print(team1,team2)
	#driver.stop_client()
driver.close()