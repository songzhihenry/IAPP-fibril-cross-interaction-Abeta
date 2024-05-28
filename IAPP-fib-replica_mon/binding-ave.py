#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:22:02 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt

font_label = 20
font_tick = 15
cv = np.loadtxt('./cv.dat')[:,1]
cv_err = np.loadtxt('./cv.dat')[:,3]

mask=[np.loadtxt('./condi/endct/ave_mask.dat')[:,1]]
mask.append(np.loadtxt('./condi/sidect/ave_mask.dat')[:,1])
'''
mask.append(mask[0]+mask[1])
temp = np.loadtxt('./condi/endct/ave_mask.dat')[:,0]
label = ['E binding','L binding','Total binding']
fig,axes = plt.subplots(figsize=(12,8),ncols=1,nrows=2)
axes[0].plot(temp,cv)
axes[0].errorbar(temp,cv,yerr=cv_err**0.5,fmt='none',capsize=1,ecolor='grey')
axes[0].set_ylabel('heat capacity (kcal/mol)',fontsize=font_label)
for i in [0,1,2]:
    axes[1].plot(temp,mask[i],label=label[i])
axes[1].set_xlabel('temp. (K)',fontsize=font_label)
axes[1].set_ylabel('probability',fontsize=font_label)
axes[1].legend(frameon=False,fontsize=font_label)
for i in [0,1]:
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
plt.savefig('cv_binding.png',dpi=220)
'''
mask.append(np.ones(100))
data = [np.loadtxt('./condi/endct/ave_rg.dat').T]
data.append(np.loadtxt('./condi/sidect/ave_rg.dat').T)
data.append(np.loadtxt('../../../monomer/replica_Ab/alldata/ave_rg.dat').T)
temp = np.loadtxt('./condi/endct/ave_mask.dat')[:,0]
label = ['@ elongation','@ lateral','ctrl']
colors = ['#1f77b4', '#ff7f0e','#2ca02c']
fig,axes = plt.subplots(figsize=(12,8),ncols=1,nrows=2)
axes[0].plot(temp,cv)
axes[0].errorbar(temp,cv,yerr=cv_err**0.5,fmt='none',capsize=1,ecolor='grey')
axes[0].set_ylabel('heat capacity (kcal/mol)',fontsize=font_label)
for i in [0,1,2]:
    y = data[i][1]
    err = data[i][2]
    axes[1].plot(temp,y/mask[i],label=label[i],color=colors[i])
    axes[1].errorbar(temp, y/mask[i],yerr=(err/16)**0.5,capsize=1,ecolor='lightgrey')
axes[1].set_xlabel('temp. (K)',fontsize=font_label)
axes[1].set_ylabel('rg (Å)',fontsize=font_label)
axes[1].legend(frameon=False,fontsize=font_label)
for i in [0,1]:
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
plt.savefig('cv_rg.png',dpi=220)
#'''