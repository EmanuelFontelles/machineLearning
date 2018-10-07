import pandas as pd
import sys
from os import system
sys.path.append('../final_project/')
sys.path.append('../')

def readNames(inputFile='new_poi_names.txt'):
    '''
    A function to read names data from a file create by a data cache

    Returns:
        Returns a data frame that contains data from 'poi_names.txt'
    '''


    #bash_command = 'bash script.sh'
    #system(bash_command)

    data = pd.read_csv(inputFile, skiprows=2, delimiter=';', header=None, names=['Ans', 'Name'])
    return(data)