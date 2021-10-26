import constants
import copy


#clean data function
def clean_data():
	#create new list so as not to overwrite 'constants.py'
	#also change information into usable integers and booleans
	clean_list = copy.deepcopy(constants.PLAYERS)
	loop_thru = 0
	stop_loop = len(constants.PLAYERS)
	while loop == True:
		clean_list[loop_thru]['height'] = clean_list[loop_thru]['height'].removesuffix(" inches")
		clean_list[loop_thru]['height'] = int(clean_list[loop_start]['height'])
		



#balance teams function
def balance_teams


if __name__ == "__main__":

