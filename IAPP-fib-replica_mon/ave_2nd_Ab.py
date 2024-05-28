#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:16:47 2021

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
def SEM(array):
    m = len(array)
    sigma = np.sqrt(array/(m-1))
    return sigma
def get_RW_2nd(data,ith_resn,stru_type):
    if stru_type == 0:
        result = ([x[ith_resn] for x in data].count('H')+[x[ith_resn] for x in data].count('G')+[x[ith_resn] for x in data].count('I'))/len(data)*100
    if stru_type == 1:
        result = ([x[ith_resn] for x in data].count('E')+[x[ith_resn] for x in data].count('B'))/len(data)*100
    if stru_type == 2:
        result = ([x[ith_resn] for x in data].count('S')+[x[ith_resn] for x in data].count('T'))/len(data)*100
    if stru_type == 3:
        result  = [x[ith_resn] for x in data].count('C')/len(data)*100
    return result
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

stru_name = ['helix','β sheet','turn','coil']

Ab_ctrl = np.zeros((4,42,50))
'''
for j in range(50):
    data = [line.strip('\n').split()[1].split('!')[0] for line in open ('../../monomer/Abeta/2ndst/{}.dssp'.format(j+1)) if not line.startswith('#')]
    for i in range(42):
        for q in range(4):
            Ab_ctrl[q][i][j] = get_RW_2nd(data,i,q)
''

for j in range(50):
    if j == 33:
        continue
    data = []
    for n in [14,16,18,20]:
        data.extend([line.strip('\n').split()[1].split('!')[0] for line in open ('2ndst/{}-{}m.dssp'.format(j+1,n)) if not line.startswith('#')])
    for i in range(42):
        for q in range(4):
            Ab_RW[q][i][j] = get_RW_2nd(data,i,q)

for j in range(50):
    if j == 46:
        continue
    data = [line.strip('\n') for line in open ('./infinit-fibril/inf_2ndst/{}.dssp'.format(j+1))][-100000:]
    for i in range(42):
        for q in range(4):
            Ab_RW[q][i][j] = get_RW_2nd(data,i,q)
#Ab_RW = np.delete(Ab_RW,33,axis=2)
'''
seq = np.arange(1,43)
#'''
Ab_ctrl = [np.loadtxt(f'../../monomer/replica_Ab/RW_{i}_300.txt')[:,0]*100 for i in ['HE','BT','TN','UT']]
Ab_ctrl_err = [np.loadtxt(f'../../monomer/replica_Ab/RW_{i}_300.txt')[:,1]*100 for i in ['HE','BT','TN','UT']]
endct_RW = [np.loadtxt('./condi/endct/RW_{}_300.txt'.format(i))[:,0]*100 for i in ['HE','BT','TN','UT']]
endct_RW_err = [np.loadtxt('./condi/endct/RW_{}_300.txt'.format(i))[:,1]*100 for i in ['HE','BT','TN','UT']]
mask_end = np.loadtxt('./condi/endct/ave_mask.dat')[25,1]
endct_RW = [x/mask_end for x in endct_RW]
sidect_RW = [np.loadtxt('./condi/sidect/RW_{}_300.txt'.format(i))[:,0]*100 for i in ['HE','BT','TN','UT']]
sidect_RW_err = [np.loadtxt('./condi/sidect/RW_{}_300.txt'.format(i))[:,1]*100 for i in ['HE','BT','TN','UT']]
mask_side = np.loadtxt('./condi/sidect/ave_mask.dat')[25,1]
sidect_RW = [x/mask_side for x in sidect_RW]

resn = list('DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVIA')
#colors = ['#1f77b4', '#ff7f0e']
fig, axes = plt.subplots(figsize=(16,9), nrows=2, ncols=2)
plt.subplots_adjust(hspace=0.2,wspace=0.2)
axes = axes.flat
fontsize_title = 24
fontsize_label = 20
fontsize_tick = 16
for q in range(4):   

    axes[q].plot(seq,Ab_ctrl[q],color=colors[0],label='ctrl',linewidth=2)
    axes[q].plot(seq,endct_RW[q],color=colors[1],label='IaF E binding',linewidth=2)
    axes[q].plot(seq,sidect_RW[q],color=colors[2],label='IaF L binding',linewidth=2)

    axes[q].errorbar(seq,Ab_ctrl[q], yerr = SEM(Ab_ctrl_err[q]),fmt='none',ecolor='grey',elinewidth=1,capsize=2)
    axes[q].errorbar(seq,endct_RW[q], yerr = SEM(endct_RW_err[q]),fmt='none',ecolor='grey',elinewidth=1,capsize=2)
    axes[q].errorbar(seq,sidect_RW[q], yerr = SEM(sidect_RW_err[q]),fmt='none',ecolor='grey',elinewidth=1,capsize=2)

    axes[q].set_title(stru_name[q],fontsize=fontsize_title)
    axes[q].tick_params(labelsize=fontsize_tick)
for i in range(2):
    axes[i*2].set_ylabel('propensity (%)',fontsize=fontsize_label)
    axes[i+2].set_xlabel('Aβ reisude index',fontsize=fontsize_label)
axes[3].legend(frameon=False, fontsize=fontsize_label)
plt.show()
#plt.savefig('ave_2nd_Ab.png', dpi=300)