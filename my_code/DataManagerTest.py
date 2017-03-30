#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from zDataManager import zDataManager
input_dir = "../public_data"
output_dir = "../res"

    
basename = 'movierec'
D = zDataManager(basename, input_dir)
print D
    
D.DataStats('train')
D.ShowScatter(1, 2, 'train')
