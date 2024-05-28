#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:30:18 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
surface = ['endct','sidect','ctrl']
name = ['elongation','lateral','ctrl']
data = [np.loadtxt('./condi/endct/ave_rg.dat').T]
data.append(np.loadtxt('./condi/sidect/ave_rg.dat').T)
data.append(np.loadtxt('../../../monomer/replica_Ab/alldata/ave_rg.dat').T)
colors = ['#1f77b4', '#ff7f0e','#2ca02c']
font_label = 20
font_tick = 15
mask=[np.loadtxt('./condi/endct/ave_mask.dat')[:,1]]
mask.append(np.loadtxt('./condi/sidect/ave_mask.dat')[:,1])
mask.append(np.ones(100))
plt.figure(figsize=(8,6))
for i in range(3):
    temp = data[i][0]
    y = data[i][1]
    err = data[i][2]
    plt.plot(temp, y/mask[i],label=name[i],color=colors[i],linewidth=3)
    plt.errorbar(temp, y/mask[i],yerr=(err/16)**0.5,capsize=1,ecolor='lightgrey')
plt.xlim(287,426)
plt.tick_params(labelsize=font_tick)
plt.ylabel('rg (Å)',fontsize=font_label)
plt.legend(frameon=False,fontsize=font_label)
plt.xlabel('Temp. (K)',fontsize=font_label)
plt.savefig('rg.png')