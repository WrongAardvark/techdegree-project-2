import constants
from copy import deepcopy

players_list = deepcopy(constants.PLAYERS)
teams_list = deepcopy(constants.TEAMS)


#clean data function
def clean_data():
	for player in players_list:
		height = player['height'].removesuffix(" inches")
		player['height'] = int(height[0])
		if player['experience'] == 'YES':
			player['experience'] = True
		if player['experience'] == 'NO':
			player['experience'] = False


#balance teams function
def balance_teams():
	


if __name__ == "__main__":
	clean_data()
	print(players_list)


