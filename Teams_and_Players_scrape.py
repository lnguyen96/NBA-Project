import bs4
import unicodedata
from unidecode import unidecode
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters'

#connection to page, download page
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each team table
containers = page_soup.findAll("table",{"class":"toccolours"})

filename = 'players.csv'
f = open(filename, 'w')
headers = 'Team, Position, Player Name, Height, Weight, Birth Date\n'
f.write(headers)

for container in containers:

	# i.e. Boston Celtics rostervte
	team_container = container.div.text
	temp = team_container.split(' ')
	temp = temp[:-1]
	team_name = ' '.join(temp)

	# gets all other info, ill comment this doodoo later
	player_containers = container.findAll('table', {'class':'sortable'})
	info_container = player_containers[0].findAll('td')
	i = 0
	for info_line in info_container:
		if i%7 == 0:
			position = info_line.text
			position = position.strip()
			i += 1
		elif i%7 == 2:
			player_name = info_line.text
			player_name = player_name.replace(',','').strip()
			player_name = player_name.split('(')
			player_name = player_name[0].split()
			if len(player_name) == 3:
				player_name = player_name[1] + ' ' + player_name[2] + ' ' + player_name[0]
			elif len(player_name) == 2:
				player_name = player_name[1] + ' ' + player_name[0]
			else:
				player_name = player_name[0]
			player_name = unicodedata.normalize('NFKD', player_name).encode('ASCII', 'ignore')
			player_name = player_name.decode('utf-8')
			i += 1
		elif i%7 == 3:
			height = info_line.text
			height = height[20:].strip()
			i += 1
		elif i%7 == 4:
			weight = info_line.text.strip()
			i += 1
		elif i%7 == 5:
			birth_date = info_line.text.strip()
			i += 1
		elif i%7 == 6:
			f.write(team_name + ',' + position + ',' + player_name + ',' + height + ',' + weight + ',' + birth_date + '\n')
			i += 1
		else:
			i += 1

f.close()