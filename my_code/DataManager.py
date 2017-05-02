#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
"""

# Add the sample code in the path
mypath = "../sample_code"
from sys import argv, path
from os.path import abspath
path.append(abspath(mypath))

# Graphic routines
import seaborn as sns; sns.set()

# Data types
import pandas as pd

# Mother class
import data_manager

class DataManager(data_manager.DataManager):
       
#    def __init__(self, basename="", input_dir=""):
#        ''' New contructor.'''
#        DataManager.__init__(self, basename, input_dir)
        # So something here
    
    def toDF(self, set_name):
        ''' Change a given data subset to a data Panda's frame.
            set_name is 'train', 'valid' or 'test'.'''
        DF = pd.DataFrame(self.data['X_'+set_name])
        # For training examples, we can add the target values as
        # a last column: this is convenient to use seaborn
        # Look at http://seaborn.pydata.org/tutorial/axis_grids.html for other ideas
        if set_name == 'train':
            Y = self.data['Y_train']
            DF = DF.assign(target=Y)          
        return DF

    def DataStats(self, set_name):
        ''' Display simple data statistics'''
        DF = self.toDF(set_name)
        print DF.describe()
    
    

    def ShowViolinplot(self,dn,x1,y1):
        #"age_25-34"    "age_45-49","age_50-55","age_56+" 
        g = sns.PairGrid(dn,
                 x_vars=[x1],
                 y_vars=[y1],
                 aspect=.75, size=3.5)
        g.map(sns.violinplot,palette="pastel");
    

if __name__=="__main__":
    # We can use this to run this file as a script and test the DataManager
    if len(argv)==1: # Use the default input and output directories if no arguments are provided
        input_dir = "../public_data"
        output_dir = "../res"
    else:
        input_dir = argv[1]
        output_dir = argv[2];
        
    print("Using input_dir: " + input_dir)
    print("Using output_dir: " + output_dir)
    
    basename = 'movierec'
    D = DataManager(basename, input_dir)
    print D
    