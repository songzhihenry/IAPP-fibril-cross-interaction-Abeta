#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:48:45 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def get_ctmap(data,row,col):
    #data = np.loadtxt('{}'.format(path))
    ctmap = np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            ctmap[i,j] = data[i*col+j]
    return ctmap
fontsize_label = 14
fontsize_title = 18
fontsize_tick = 12
data = get_ctmap(np.loadtxt('RW_endctm_300.txt')[:,0],24,42)
cmap=cm.Greys
plt.imshow(data,cmap=cmap,origin='lower')
plt.xticks(np.linspace(0,41,8,dtype=int),np.linspace(0,41,8,dtype=int)+1,fontsize=fontsize_tick)
plt.yticks(np.linspace(0,23,6,dtype=int),np.linspace(0,23,6,dtype=int)+14,fontsize=fontsize_tick)