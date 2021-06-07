'''
Created on May 14, 2021

Randomly generates an arbitrary, user-defined number of characters for use
in the Chronicle of Darkness roleplaying system, using logic for a given
user-selected gameline.

Characters are stored in a JSON file for later use, as well as a more human 
readable plain text file.

@author: Fred
'''
import json
import mage

if __name__ == '__main__':
    city = input('Please name the city you are generating:')
    pop = ''
    while not pop.isdigit(): #We won't accept an answer unless it is valid! Valid answers are positive integers.
        pop = input('Please select a population size:')
    pop = int(pop) #we convert it to an integer for later use
    game = ''
    valid_options = ['mage']
    while game not in valid_options:
        game = input('Gameline:').lower()
    file_name = city + '_' + game
    if game == 'vampire':
        pass
    elif game == 'werewolf':
        pass
    elif game == 'mage':
        print('Generating Mage: The Awakening NPCS')
        results = mage.main(pop)
        #We are dumping a JSON file for later use in constructing stuff like pie charts.
        print('Dumping Mage: The Awakening NPCs to JSON file ' + file_name + '.json')
        with open('./output/'+file_name+'.json', 'x') as f:
            json.dump(results, f)
        #And now we are putting the stuff into a human readable format for actual use.
        print('Dumping Mage: the Awakening NPCs in readable format to ' + file_name + '.txt')
        with open('./output/'+file_name+'.txt', 'x') as f:
            f.write(mage.formatter(results))
    else:
        print('Error: Selected option was accepted, but has no associated methods.')
    graphing = input('Would you like to generate graphs of this city? If so, type "y". Any other response will exit.').lower()
    if graphing == 'y':
        if game == 'vampire':
            pass
        elif game == 'werewolf':
            pass
        elif game == 'mage':
            mage.grapher('./output/'+file_name, results)