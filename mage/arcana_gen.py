'''
Created on May 14, 2021

@author: Fred
'''
import random

def gen(path, gnosis):
    path_list = {'Acanthus' : ['Fate', 'Time'],
                 'Mastigos' : ['Mind', 'Space'],
                 'Moros' : ['Matter', 'Death'],
                 'Obrimos' : ['Forces', 'Prime'],
                 'Thyrsus' : ['Spirit', 'Life']}
    arcana_list = ['Fate', 'Time', 'Mind', 'Space', 'Matter', 'Death', 'Forces', 'Prime', 'Spirit', 'Life']
    sorted(arcana_list)
    non_ruling = [] #we now identify all the non-ruling arcana
    for field in arcana_list:
        if field not in path_list[path]:
            non_ruling.append(field)
    arcana_max = get_arcana_max(gnosis) #May have one arcana at this value
    other_max = get_other_max(gnosis) #May have any other arcana at this value
    results = {}
    for n in arcana_list:
        results[n] = 0
    for n in path_list[path]: #we start by giving them 2 points in their ruling arcana
        results[n] = 2
    results[random.choice(path_list[path])] += 1 #we randomly increase one to 3
    results[random.choice(non_ruling)] = 1 #we give them 1 point in a non-ruling arcana
    if gnosis > 1: #if gnosis is 1, then we've already finished
        points = gnosis * 3
        while points > 0:
            choice = random.choice(arcana_list)
            if results[choice] < other_max or (results[choice] < arcana_max and check_max(arcana_max, results) == 0):
                results[choice] += 1
                points -= 1
    
    return(results)

def get_arcana_max(gnosis):
    gnosis_to_max = {1 : 3,
                     2 : 3,
                     3 : 4,
                     4 : 4,
                     5 : 5}
    if gnosis <= 5:
        return gnosis_to_max[gnosis]
    else:
        return 5

def get_other_max(gnosis):
    gnosis_to_other = {1 : 2,
                       2 : 3,
                       3 : 3,
                       4 : 4,
                       5 : 4}
    if gnosis <= 5:
        return gnosis_to_other[gnosis]
    else:
        return 5
    
def check_max(arcana_max, arcana_list):
    results = []
    for n in arcana_list:
        if n == arcana_max:
            results.append(1)
        else:
            results.append(0)
    return sum(results)