# =========================
# This file contains a function to loop through the dataframe and return target players
# =========================



# Function will loop through the rows in the dataframe
# It will then loop through the players in the teams listed 
# Using the function 'identify_nsubj_pobj' it will identify players listed in the sentence from their player identifiers listed in 'players dictionary'
# It will add a list of the target players to the dataframe's corresponding row
# Finally it will return a dataframe in which rows without target players have been removed


#__Note__: 
# Problems still occur when players have the same surname


# =============
#  IMPORTS 
# =============


# Local imports
import modules.players_dictionary as players_dictionary
import modules.identify_nsubj_pobj as identify_nsubj_pobj



# =============
#  The Function
# =============

def target_identifier(dictionary):
    
    # Define an empty players list
    player_list = []
    

        
    # Create an empty dictionary to store players as keys and player identifiers as values
    d = {}

    # Iterate through the teams listed in each row
    for team in dictionary['teams']:

    	# Save the dictionary of squad players from the 'players_dictionary' module that match each team listed in the row
        squad_players = players_dictionary.premier_league_players_dictionary[team]['squad_players']

        # Make a dictionary holding the players names and player identifiers = d
        for player_key, player_value in squad_players.items():
            d[player_key] = player_value['identifiers']

    # Use the identify_nsubj_pobj function to return a list of the target players in the phrase      
    if identify_nsubj_pobj.identify_nsubj_pobj(dictionary['phrase'], d):
    	# If there is a match --->  Append the player targets to the player_list
        player_list.append(identify_nsubj_pobj.identify_nsubj_pobj(dictionary['phrase'], d))
    else: 
    	# If there is no match ----> Append and empty string
        player_list.append("")
    
    # Add the flattened players list to a new key in the dictionary
    dictionary['targets'] = [y for x in player_list for y in x]
    

    # Return the dictionary to be filtered and processed in the pipeline
    return dictionary