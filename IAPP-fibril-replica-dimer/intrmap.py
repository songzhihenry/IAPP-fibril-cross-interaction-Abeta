#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:40:50 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
fontsize_label = 16
fontsize_title = 18
fontsize_tick = 12
cmap=cm.bwr
mask_end = np.loadtxt('./end/ave_mask.dat')[9,1]
mask_side = np.loadtxt('./side/ave_mask.dat')[9,1]
mask_ctrl = np.loadtxt('../../dimer/replica_Ab/condi/ave_mask.dat')[9,1]
ctrl = np.loadtxt('../../dimer/replica_Ab/condi/RW_inctm_300.txt')[:,0]/mask_ctrl
end_data = np.loadtxt('./end/RW_inctm_300.txt')[:,0]/mask_end
side_data = np.loadtxt('./side/RW_inctm_300.txt')[:,0]/mask_side

map2 = np.zeros((42,42))
map3 = np.zeros((42,42))
map5 = np.zeros((42,42))
for i in range(1,43):
    for j in range(i,43):
        if i == j:
            map2[i-1,j-1] = 0.5
            map3[i-1,j-1] = 0.5
            map5[i-1,j-1] = 0.5
        else:
            map2[i-1,j-1] = end_data[j-i+int((84-i)*(i-1)/2)-1]
            map3[i-1,j-1] = side_data[j-i+int((84-i)*(i-1)/2)-1]
            map5[i-1,j-1] = ctrl[j-i+int((84-i)*(i-1)/2)-1]
ctm_end = map2.transpose()+map5
ctm_side = map3.transpose()+map5
ctm = [np.where(x>=0.99,0,x) for x in [ctm_end,ctm_side]]
titles = ['E binding (left) & Ctrl (right)','L binding (left) & Ctrl (left)']
fig, axes = plt.subplots(figsize=(12,6),nrows=1, ncols=2);axes = axes.flatten()
for ax,ct,title in zip(axes,ctm,titles):
    htm = ax.imshow(ct,cmap=cmap,origin='lower')
    ax.set_xticks(np.linspace(0,41,8,dtype=int))
    ax.set_xticklabels(np.linspace(0,41,8,dtype=int)+1,fontsize=fontsize_tick)
    ax.set_yticks(np.linspace(0,41,8,dtype=int))
    ax.set_yticklabels(np.linspace(0,41,8,dtype=int)+1,fontsize=fontsize_tick)
    ax.set_title(title,fontsize=fontsize_title)
    cb = plt.colorbar(htm,ax=ax, fraction=0.1,shrink=0.6)
for i in range(2):
    axes[i].set_xlabel('Aβ residue index',fontsize=fontsize_label)
axes[0].set_ylabel('Aβ residue index',fontsize=fontsize_label)
cb.set_label('Frequency',fontsize=fontsize_label)
cb.ax.tick_params(labelsize=fontsize_tick)
plt.savefig('intrachain-ctmap.png',dpi=220)