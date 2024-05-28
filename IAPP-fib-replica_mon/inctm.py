#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:24:55 2022

@author: zhiyuas
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
fontsize_label = 16
fontsize_title = 18
fontsize_tick = 12
cmap=cm.bwr
ctrl = np.loadtxt('../../../monomer/replica_Ab/alldata/RW_inctm_300.txt')[:,0]
#all_data = np.loadtxt('RW_inctm_300.txt')[:,0]
mask_end = np.loadtxt('./condi/endct/ave_mask.dat')[17,1]
mask_side = np.loadtxt('./condi/sidect/ave_mask.dat')[17,1]
end_data = np.loadtxt('./condi/endct/RW_inctm_300.txt')[:,0]/mask_end
side_data = np.loadtxt('./condi/sidect/RW_inctm_300.txt')[:,0]/mask_side
#end_data = np.mean(np.loadtxt('./condi/endct/inctm_300.txt'),axis=0)
#side_data = np.mean(np.loadtxt('./condi/sidect/inctm_300.txt'),axis=0)
#inf_side_data = np.loadtxt('../infinit-fibril/intra_ctm.txt')/50
#map1 = np.zeros((42,42))
map2 = np.zeros((42,42))
map3 = np.zeros((42,42))
map4 = np.zeros((42,42))
map5 = np.zeros((42,42))
for i in range(1,43):
    for j in range(i,43):
        if i == j:
            #map1[i-1,j-1] = 0.5
            map2[i-1,j-1] = 0.5
            map3[i-1,j-1] = 0.5
            map4[i-1,j-1] = 0.5
            map5[i-1,j-1] = 0.5
        else:
            #map1[i-1,j-1] = all_data[j-i+int((84-i)*(i-1)/2)-1]
            map2[i-1,j-1] = end_data[j-i+int((84-i)*(i-1)/2)-1]
            map3[i-1,j-1] = side_data[j-i+int((84-i)*(i-1)/2)-1]
            #map4[i-1,j-1] = inf_side_data[j-i+int((84-i)*(i-1)/2)-1]
            map5[i-1,j-1] = ctrl[j-i+int((84-i)*(i-1)/2)-1]
#ctm_all = map1.transpose()+map5
ctm_end = map2.transpose()+map5
ctm_side = map3.transpose()+map5
#ctm_inf_side = map4.transpose()+map5
ctm = [np.where(x>=0.9,0,x) for x in [ctm_end,ctm_side]]
#vmin=0; vmax=max([np.max(x) for x in ctm])
#titles = ['Overall (left) & Ctrl (right)','elongation binding (left) & Ctrl (right)',\
          #'lateral binding (left) & Ctrl (left)','lateral binding (left) & Ctrl (left) on inf fib']
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
    axes[i].set_xlabel(r'Aβ residue index',fontsize=fontsize_label)
axes[0].set_ylabel('Aβ residue index',fontsize=fontsize_label)
#cb = plt.colorbar(htm, ax=axes, fraction=0.1,shrink=0.6)
cb.set_label('Frequency',fontsize=fontsize_label)
cb.ax.tick_params(labelsize=fontsize_tick)
plt.savefig('condi-ctmap.png')