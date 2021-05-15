'''
Created on May 14, 2021
Randomly generates an arbitrary, user-defined number of characters for use
in a Mage: The Awakening Second Edition consilium. 

Once the consilium has been generated, utilizes matplotlib to create pie
charts indicating key information regarding the consilium's demographics.
Namely: Breakdown of all paths, breakdown of paths within pentacle, and 
breakdown of Order demographics.

Characters are generated with the following attributes:
    Shadow Name
    Character Age (18-70)
    Gnosis
    Path
    Order
    Arcana, based on Path, Gnosis and Legacy

@author: Fred
'''
import random
import mage.shadow_names as shadow_names
import mage.order_picker as order
import mage.arcana_gen as arcana

def main(pop):
    '''The core function for the Mage: The Awakening generator.
    Calls on a number of other functions in order to generate the characters
    for this gameline.
    
    Returns a dictionary of dictionary. Dictionary key is a randomly generated
    'shadow name' for the character, the value dictionary contains
    their age (int), gnosis (int 1-10), path (str), legacy (str), arcana (dictionary), 
    and mentor (string).
    
    Args
    ----
    pop : int
        an integer representing the number of characters to be generated
    '''
    consilium = {} #creating a blank dictionary for later use
    names = name_list(pop)
    for n in names:  #we start by naming every character generated
        consilium[n] = {} #and creating a dictionary entry for them
    for char in consilium:
        consilium[char]['Gnosis'] = gnosis_gen()
        consilium[char]['Path'] = random.choice(['Acanthus', 'Mastigos', 'Moros', 'Obrimos', 'Thyrsus'])
        consilium[char]['Order'] = order.gen()
        consilium[char]['Arcana'] = arcana.gen(consilium[char]['Path'], consilium[char]['Gnosis'])
    return consilium

def name_list(pop):
    '''Calls on the logic in shadow_names in order to generate an arbitrary
    number of unique names.
    
    Returns a list of strings

    Args
    ----
    pop : int
        an integer representing the number of characters to be generated
    '''
    name_list = []
    for _ in range(pop):
        name = shadow_names.gen() #we generate an initial shadow name to check
        while name in name_list: #if the name exists, we continue to generate until it is unique
            name = shadow_names.gen()
        name_list.append(name) #we add the unique name to the list
    return name_list

def gnosis_gen():
    '''Generates a random value for the character's gnosis. Each character 
    begins with a 100% chance of receiving their 1st point of gnosis, with 
    that chance then steadily decreasing by a given value, defined in 
    pct_dec.
    
    If they fail the roll, they remain at that value.
    
    returns an int
    '''
    pct_dec = 15
    chance = 100
    gnosis = 0
    while chance > 0:
        rand = random.randint(1,100)
        if rand <= chance:
            gnosis += 1
            chance -= pct_dec
        else:
            break
    return gnosis