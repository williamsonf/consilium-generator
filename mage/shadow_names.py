'''
Created on May 14, 2021
Randomly generates a shadow name for use by a Mage the Awakening character.
Shadow names are not real names, and as such they tend to come across more as
titles (The x of y, The X, The Adjective Noun, etc.)

@author: Fred
'''
import os, random

def gen():
    #We begin by generating master lists of nouns, adjectives, verbs
    current_path = os.path.dirname(__file__)
    ADJ_LIST = []
    with open(os.path.abspath(os.path.join(current_path, '..', 'lists', 'adjectives.txt')), 'r') as f:
        for line in f:
            ADJ_LIST.append(line.split('\n')[0])
    random.shuffle(ADJ_LIST)
    SING_NOUNS = []
    PLUR_NOUNS = []
    with open(os.path.abspath(os.path.join(current_path, '..', 'lists', 'nouns.txt')), 'r') as f:
        for line in f:
            line = line.split('\n')[0]
            if line[-1] == 's':
                PLUR_NOUNS.append(line)
            else:
                SING_NOUNS.append(line)
    random.shuffle(SING_NOUNS)
    random.shuffle(PLUR_NOUNS)
    PRES_VERBS = []
    PAST_VERBS = []
    with open(os.path.abspath(os.path.join(current_path, '..', 'lists', 'verbs.txt')), 'r') as f:
        for line in f:
            line = line.split('\n')[0]
            if line[-3:] == 'ing':
                PRES_VERBS.append(line)
            elif line[-2:] == 'ed':
                PAST_VERBS.append(line)
    random.shuffle(PRES_VERBS)
    random.shuffle(PAST_VERBS)

    name = ''
    if random.randint(1,100) > 50:
        name += 'The '
    if random.randint(1,100) > 75:
        name += random.choice(ADJ_LIST + PAST_VERBS).title() + ' '
    name += random.choice(SING_NOUNS).title()
    if random.randint(1,100) > 50:
        name += ' of '
        if random.randint(1,100) > 50:
            name += random.choice(ADJ_LIST + PRES_VERBS).title() + ' '
        name += random.choice(PLUR_NOUNS + SING_NOUNS).title()
    return name

if __name__ == '__main__':
    for _ in range(11):
        print(gen())