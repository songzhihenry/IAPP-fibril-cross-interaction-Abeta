#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 13:03:02 2022

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

end_data = (np.loadtxt('./end/RW_resct_300.txt')[:,0]/mask_end).reshape((42,42))
end_data  = (end_data + end_data.T)/2
side_data = (np.loadtxt('./side/RW_resct_300.txt')[:,0]/mask_side).reshape((42,42))
side_data  = (side_data + side_data.T)/2
ctrl = (np.loadtxt('../../dimer/replica_Ab/condi/RW_resct_300.txt')[:,0]/mask_ctrl).reshape((42,42))
titles = ['elongation binding','lateral binding',' Ctrl']
ctrl  = (ctrl + ctrl.T)/2
data = [end_data,side_data,ctrl]
fig,axes = plt.subplots(figsize=(18,6),nrows=1, ncols=3)
for i in range(3):
    heatm = axes[i].imshow(data[i],cmap=cmap,origin='lower')
    axes[i].set_xticks(np.linspace(0,41,8,dtype=int))
    axes[i].set_xticklabels(np.linspace(0,41,8,dtype=int)+1,fontsize=fontsize_tick)
    axes[i].set_yticks(np.linspace(0,41,8,dtype=int))
    axes[i].set_yticklabels(np.linspace(0,41,8,dtype=int)+1,fontsize=fontsize_tick)
    axes[i].set_title(titles[i],fontsize=fontsize_title)
    cb = plt.colorbar(heatm, ax=axes[i], fraction=0.035,pad=0.1)
    axes[i].set_xlabel('Aβ residue index',fontsize=fontsize_label)
axes[0].set_ylabel('Aβ residue index',fontsize=fontsize_label)
cb.set_label('Frequency',fontsize=fontsize_label)
cb.ax.tick_params(labelsize=fontsize_tick)
plt.savefig('interchain-ctmap.png',dpi=220)