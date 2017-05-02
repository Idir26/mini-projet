#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from DataManager import DataManager
input_dir = "../public_data"
output_dir = "../res"

    
basename = 'movierec'
D = DataManager(basename, input_dir)
print D
    
D.DataStats('train')
D.ShowViolinplot('data',"age_-18","movie_genre_Romance")