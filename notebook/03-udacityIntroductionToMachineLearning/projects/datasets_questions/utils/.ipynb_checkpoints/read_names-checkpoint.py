import pandas as pd
import sys
from os import system
sys.path.append('../final_project/')

def readNames():
    '''
    A function to read names data from a file create by a data cache

    Returns:
        Returns a data frame that contains data from 'poi_names.txt'
    '''

    system("cat '../final_project/poi_names.txt' | awk '{print $1';', $3" "$2}' | sed 's/,*\r*$//' > 'new_poi_names.txt'")

    return(pd.read_csv("../new_poi_names.txt", skiprows=2, delimiter=';', header=None, names=['Ans', 'Name']))