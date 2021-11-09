import constants
from copy import deepcopy

players_list = deepcopy(constants.PLAYERS)
Panthers = []
Bandits = []
Warriors = []



#clean data function
#cleans height, experience, guardians
def clean_data():
	for player in players_list:
		height = player['height'].split()
		player['height'] = int(height[0])
		if player['experience'] == 'YES':
			player['experience'] = True
		if player['experience'] == 'NO':
			player['experience'] = False
		player['guardians'] = player['guardians'].split(' and ')
		

#divide between experienced and inexperienced players
#divide teams up equally
def balance_teams():
	exp_players = []
	inexp_players= []
	for player in players_list:
		if player['experience'] == True:
			exp_players.append(player)
		if player['experience'] == False:
			inexp_players.append(player)
	for i, player in enumerate(exp_players):
		if i <= 3:
			Panthers.append(player)
		if i > 3 and i <= 6:
			Bandits.append(player)
		if i > 6:
			Warriors.append(player)
	for i, player in enumerate(inexp_players):
		if i <= 3:
			Panthers.append(player)
		if i > 3 and i <= 6:
			Bandits.append(player)
		if i > 6:
			Warriors.append(player)


def additional_stats():
	
			

if __name__ == "__main__":
	clean_data()
	balance_teams()
	print(Panthers)



