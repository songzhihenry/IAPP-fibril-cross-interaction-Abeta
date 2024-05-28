#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 08:55:56 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt

fontsize_label = 18
fontsize_title = 18
fontsize_tick = 12
fig,axes = plt.subplots(figsize=(12,8),ncols=1,nrows=2)
ctrl = np.loadtxt('../../dimer/replica_Ab/alldata/cv.dat').T
cv = np.loadtxt('./all/cv.dat').T
'''
dis_dim = np.loadtxt('../../dimer/replica_Ab/condi/ave_mask.dat').T
dis_dim_fib = np.loadtxt('./dis_dim/ave_mask.dat').T
#at_l_one = np.loadtxt('./at_least_one_on_fib/ave_mask.dat').T
data1 = [dis_dim, dis_dim_fib]#, at_l_one]
label1 = ['Dimerization -fib','Dimerization +fib']#,'At least a monomer on fibril']
axes[1].set_ylabel('Probability (kcal/mol)',fontsize=fontsize_label)
'''
#'''
beta_ctrl = np.loadtxt('../../dimer/replica_Ab/alldata/ave_betasheet.dat').T
beta = np.loadtxt('./No_mono_on_fib/ave_mask.dat').T
data1 = [beta_ctrl,beta]
label1 = ['- fib','+ fib']
axes[1].set_ylabel('β sheet content (%)',fontsize=fontsize_label)
#'''
'''
rg_ctrl = np.loadtxt('../../dimer/replica_Ab/alldata/ave_rg.dat').T
rg  = np.loadtxt('./all/ave_rg.dat').T
data1 = [rg_ctrl,rg]
label1 = ['- fib','+ fib']
'''
data = [ctrl,cv]

label = ['- fibril','+ fibrl']

for i in range(2):
    temp = data[i][0]
    cv = data[i][1]
    err = data[i][3]
    axes[0].plot(temp,cv,label=label[i])
    axes[0].errorbar(temp,cv,yerr=err**0.5,fmt='none',capsize=1,ecolor='grey')
    axes[0].legend(frameon=False,fontsize=fontsize_label)
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
for i in range(2): 
    temp = data1[i][0]
    cv = data1[i][1]
    err = data1[i][2]
    axes[1].plot(temp,cv,label=label1[i])
    axes[1].errorbar(temp,cv,yerr=(err/24)**0.5,fmt='none',capsize=1,ecolor='lightgrey')
    axes[1].legend(frameon=False,fontsize=fontsize_label)
axes[1].set_xlabel('Temperature (K)',fontsize=fontsize_label)
axes[0].set_ylabel('Cv (kcal/mol)',fontsize=fontsize_label)
plt.savefig('Cv_binding.png',dpi=220)