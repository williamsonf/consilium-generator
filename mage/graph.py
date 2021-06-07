'''
Created on Jun 7, 2021

@author: Fred
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib._color_data import BASE_COLORS

#declared globally because we use it in a few places
arcana_list = ['Fate', 'Time', 'Mind', 'Space', 'Matter', 'Death', 'Forces', 'Prime', 'Spirit', 'Life']
arcana_list = sorted(arcana_list) #lazily making it alphabetical
arcana_colors = {'Fate' : 'paleturquoise',
                 'Time' : 'dodgerblue',
                 'Mind' : 'violet',
                 'Space' : 'rebeccapurple',
                 'Matter' : 'seagreen',
                 'Death' : 'navy',
                 'Forces' : 'red',
                 'Prime' : 'yellow',
                 'Spirit' : 'orange',
                 'Life' : 'green'}

def clean_json(json):
    '''We mucked up the initial creation of the mage dictionary, so we need to
    sort everything into lists for our dataframe to make sense of.
    '''
    result = {}
    result['Name'] = [i for i in json.keys()] #first we create a dictionary key of character names
    for k in json: #next we do the same for the other values, gnosis, path, etc.
        for col in json[k]:
            if col in result.keys():
                pass
            else:
                result[col] = []
            result[col].append(json[k][col])
    for arcana in arcana_list:
        result[arcana] = []
    for k in json: #We saved even 0 values initially, so we can just load them in.
        for a in json[k]['Arcana']:
            result[a].append(json[k]['Arcana'][a])
    return result

def make_frame(json):
    return pd.DataFrame(json)

def total_charts(dataframe, filename):
    '''
    Generates charts for the total population of our fictional city.
    Displays total population by Path, Order and Gnosis.
    '''
    base_color = sb.color_palette()[0]
    
    plt.figure(figsize=[30,20])
    
    plt.subplot(2, 3, 1)
    sb.countplot(data=dataframe, x='Path', color=base_color)
    plt.xticks(rotation=60)
    plt.ylabel('Population')
    
    plt.subplot(2, 3, 2)
    sb.countplot(data=dataframe, x='Order', color=base_color)
    plt.xticks(rotation=60)
    plt.ylabel('Population')
    
    plt.subplot(2, 3, 3)
    sb.countplot(data=dataframe, x='Gnosis',  color=base_color)
    plt.ylabel('Population')
    
    plt.subplot(2,3,4)
    counts = dataframe['Path'].value_counts()
    plt.pie(counts, labels=counts.index, startangle= 90, counterclock= False)
    
    plt.subplot(2,3,5)
    counts = dataframe['Order'].value_counts()
    plt.pie(counts, labels=counts.index, startangle= 90, counterclock= False)
        
    plt.savefig(filename+'_poptotalcharts.png')
    
def order_charts(dataframe, filename):
    base_color = sb.color_palette()[0]
    order_list = dataframe['Order'].unique()
    fig, big_axis = plt.subplots(figsize=(30,50), nrows=len(order_list))
    for row, big_ax in enumerate(big_axis):
        big_ax.set_title(order_list[row] + "\n", fontsize= 16)
        big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
        big_ax._frameon = False
        
    curr_plot = 1
    for order in order_list:
        altered_frame = dataframe[dataframe['Order'].isin([order]) == True]
        ax = fig.add_subplot(len(order_list), 3, curr_plot)
        ax.set_title('Gnosis Pop')
        sb.countplot(data=altered_frame, x='Gnosis', color=base_color, order=list(range(1,11)))
        plt.yticks(np.arange(1, altered_frame['Gnosis'].value_counts().max()+1, 1)) #this is generating phantom y ticks but I dont know why, so I guess it's gonna be left like that for now.
        plt.ylabel('Population')
        curr_plot += 1
        ax = fig.add_subplot(len(order_list),3,curr_plot)
        ax.set_title('Path Pop')
        sb.countplot(data=altered_frame, x='Path', color=base_color, order=sorted(dataframe['Path'].unique()))
        plt.yticks(np.arange(1, altered_frame['Path'].value_counts().max()+1, 1))
        plt.ylabel('Population')
        curr_plot +=1
        ax = fig.add_subplot(len(order_list), 3, curr_plot)
        ax.set_title('Arcana Levels')
        altered_frame = altered_frame[arcana_list]
        arc_dic = {'Arcana' : [],
                   'Value' : []}
        for i in altered_frame:
            for n in altered_frame[i]:
                arc_dic['Arcana'].append(i)
                arc_dic['Value'].append(n)
        altered_frame = pd.DataFrame(arc_dic)
        sb.countplot(data=altered_frame, x='Arcana', hue='Value', order=arcana_list, hue_order=range(1,6)) #it looks like shit but I've spent enough time on it. Will give it another go later.
        plt.legend(loc='lower center', bbox_to_anchor=(1, 1))
        plt.ylabel('Population')
        curr_plot += 1
        
    plt.savefig(filename+'_ordercharts.png')
    
def grapher(filename, data):
    data = clean_json(data)
    frame = make_frame(data)
    print('Generating general population overview at ' + filename + '_poptotalcharts.png')
    total_charts(frame, filename)
    print('Generating Order specific overview at ' + filename + '_ordercharts.png')
    order_charts(frame, filename)