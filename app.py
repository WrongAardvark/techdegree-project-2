import constants
from copy import deepcopy

players_list = deepcopy(constants.PLAYERS)
team_list = {
'Panthers': [],
'Bandits': [],
'Warriors': []
}


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
		if i <= 2:
			team_list['Panthers'].append(player)
		if i > 2 and i <= 5:
			team_list['Bandits'].append(player)
		if i > 5:
			team_list['Warriors'].append(player)
	for i, player in enumerate(inexp_players):
		if i <= 2:
			team_list['Panthers'].append(player)
		if i > 2 and i <= 5:
			team_list['Bandits'].append(player)
		if i > 5:
			team_list['Warriors'].append(player)


def main_menu():
	run = True
	while run == True:
		print('\n-> Basketball Stats Tool <-\n===== MAIN MENU =====')
		choice_1 = input('\n - Choose from the options bellow... -\n > 1) Display Team Stats\n > 2) Quit\n\nEnter an option:  ')
		if int(choice_1) == 1:
			team_name = input('\n - Select from the teams below... -\n > 1) Panthers\n > 2) Bandits\n > 3) Warriors\n\nEnter an option:  ')
			team_name = int(team_name)-1
			if team_name == 0:
				team_name = 'Panthers'
			if team_name == 1:
				team_name = 'Bandits'
			if team_name == 2:
				team_name = 'Warriors'
			print('\n --- {} ---: \n----------'.format(team_name))
			print('\n- Total players: {}'.format(len(team_list[team_name])))
			names = []
			for player in team_list[team_name]:
				names.append(player['name'])
			print('\n- Players on team:\n {}'.format(', '.join(names))+'\n')
			choice_3 = input('\n- Choose from the options below...\n > 1) Additional Stats for the {}\n > 2) Return to Menu\n\nEnter an option:  '.format(team_name))
			# Additional stats number of inexperienced/experienced players, average height of players, guardians of team
			if int(choice_3) == 1:
				team_height = []
				for player in team_list[team_name]:
					team_height.append(player['height'])
				average_height = sum(team_height) / len(team_name)
				print('\n- Average Height of Team:  {} inches'.format(average_height))
				exp_players = 0
				inexp_players = 0
				for player in team_list[team_name]:
					if player['experience'] == True:
						exp_players += 1
					else:
						inexp_players +=1
				print('- There are {} experienced players and {} inexperienced players on this team.'.format(exp_players, inexp_players))
				print('- The guardians on this team are as follows:\n')
				for player in team_list[team_name]:
    					print(' Player: {} | Guardian(s): {}'.format(player['name'], ', '.join(player['guardians'])))
			else:
				continue

		elif int(choice_1) == 2:
			print('\n\nThanks for using the Basketball Stats Tool!\n')
			run = False

		else:
			print("\nPlease enter a valid option...")



if __name__ == "__main__":
	clean_data()
	balance_teams()
	main_menu()



