#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:56:23 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
fontsize_label = 16
fontsize_title = 18
fontsize_tick = 12
def SEM(array,replica):
    return (array/replica)**0.5
E = [np.loadtxt('./end/RW_{}_300.txt'.format(i)).T*100 for i in ['HE','BT']]
L = [np.loadtxt('./side/RW_{}_300.txt'.format(i)).T*100 for i in ['HE','BT']]
C = [np.loadtxt('../../dimer/replica_Ab/condi/RW_{}_300.txt'.format(i)).T*100 for i in ['HE','BT']]
mask = [np.loadtxt('./end/ave_mask.dat')[9,1]]
mask.append(np.loadtxt('./side/ave_mask.dat')[9,1])
mask.append(np.loadtxt('../../dimer/replica_Ab/condi/ave_mask.dat')[9,1])
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
fig,axes = plt.subplots(figsize=(14,5),ncols=2,nrows=1)
resn = np.arange(1,85)
resn = np.arange(1,43)
stru = ['helices','β sheets']
groups = ['@ E fib','@ L fib', '- fib']

for q in range(2):
    axes[q].plot(resn, (E[q][0][:42]+E[q][0][-42:])/2/mask[0],label=groups[0],color=colors[0],linewidth=2)
    axes[q].errorbar(resn, (E[q][0][:42]+E[q][0][-42:])/2/mask[0],yerr=SEM(E[q][1][:42]+E[q][1][-42:],48),fmt='none',capsize=1,ecolor='grey')
    axes[q].plot(resn, (L[q][0][:42]+L[q][0][-42:])/2/mask[1],label=groups[1],color=colors[1],linewidth=2)
    axes[q].errorbar(resn, (L[q][0][:42]+L[q][0][-42:])/2/mask[1],yerr=SEM(L[q][1][:42]+L[q][1][-42:],48),fmt='none',capsize=1,ecolor='grey')
    axes[q].plot(resn, (C[q][0][:42]+C[q][0][-42:])/2/mask[2],label=groups[2],color=colors[2],linewidth=2)
    axes[q].errorbar(resn, (C[q][0][:42]+C[q][0][-42:])/2/mask[2],yerr=SEM(C[q][1][:42]+C[q][1][-42:],48),fmt='none',capsize=1,ecolor='grey')
for i in range(2):
    axes[i].set_xlabel('Aβ residue index',fontsize=fontsize_label)
    axes[i].set_title(stru[i],fontsize=fontsize_title)
axes[0].set_ylabel('content (%)',fontsize=fontsize_label)
axes[0].legend(frameon=False,fontsize=fontsize_label)
plt.savefig('RW_2nd.png',dpi=220)