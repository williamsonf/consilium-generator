'''
Created on May 14, 2021

@author: Fred
'''

def formatter(mage_list):
    string = ''
    for n in mage_list:
        string += '{} (Gnosis: {}, Path: {}, Order: {})\n'.format(n,
                                                                  str(mage_list[n]['Gnosis']),
                                                                  mage_list[n]['Path'],
                                                                  mage_list[n]['Order'])
        string += "Arcana: " + arcana_lister(mage_list[n]['Arcana']) + "\n\n"
    return string

def arcana_lister(arcana):
    #let's start by removing all the junk arcana from the list
    arcana = {key:val for key, val in arcana.items() if val > 0}

    #Next we're going to sort them by their values.
    sorted_values = sorted(arcana.values(), reverse=True)
    sorted_arcana = {}    
    for v in sorted_values:
        for k in arcana.keys():
            if arcana[k] == v:
                sorted_arcana[k] = v
                
    #finally, we'll construct a string listing them all
    string_list = []
    for arcana in sorted_arcana:
        string_list.append(str(arcana) + ' ' + str(sorted_arcana[arcana]))
    return ", ".join(string_list)