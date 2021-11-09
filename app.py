import constants
from copy import deepcopy

players_list = deepcopy(constants.PLAYERS)
teams_list = deepcopy(constants.PLAYERS)


#clean data function
def clean_data():
	for player in players_list:
		height = player['height'].split()
		player['height'] = int(height[0])
		if player['experience'] == 'YES':
			player['experience'] = True
		if player['experience'] == 'NO':
			player['experience'] = False

#
def balance_teams():
	exp_players = []
	inexp_players= []
	for player in players_list:
		if player['experience'] == True:
			exp_players.append(player)
		if player['experience'] == False:
			inexp_players.append(player)
	for index, player in enumerate(exp_players):
		if player

if __name__ == "__main__":
	clean_data()
	balance_teams()
	print(exp_players)


