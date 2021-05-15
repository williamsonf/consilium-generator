'''
Created on May 14, 2021

@author: Fred
'''
import os, random

def gen():
    current_path = os.path.dirname(__file__)
    ORDERS = []
    with open(os.path.abspath(os.path.join(current_path, '..', 'lists', 'mage_orders.txt')), 'r') as f:
        for line in f:
            line = line.split('\n')[0]
            line = tuple(line.split(','))
            ORDERS.append(line)
    return random.choices([n[0] for n in ORDERS], weights=[int(n[1]) for n in ORDERS])[0]