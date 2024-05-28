#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:10:39 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt

fontsize_label = 14
fontsize_title = 18
fontsize_tick = 12

dis_dim = np.loadtxt('../../dimer/replica_Ab/condi/ave_mask.dat').T
dis_dim_fib = np.loadtxt('./dis_dim/ave_mask.dat').T
at_l_one = np.loadtxt('./at_least_one_on_fib/ave_mask.dat').T

#end_data = np.loadtxt('./alldata/cv.dat').T
#side_data = np.loadtxt('../IAPP-fib-replica_dimer_L/alldata/cv.dat').T
#data = [end_data,side_data,ctrl]
data = [dis_dim, dis_dim_fib, at_l_one]
label = ['Dimer disassocation','Dimer disassocation +fib','At least one on fibrl']
for i in range(3):
    temp = data[i][0]
    cv = data[i][1]
    err = data[i][2]
    plt.plot(temp,cv,label=label[i])
    plt.errorbar(temp,cv,yerr=(err/24)**0.5,fmt='none',capsize=1,ecolor='lightgrey')
plt.legend(frameon=False)
plt.xlabel('Temperature (K)',fontsize=fontsize_label)
plt.ylabel('Probability (kcal/mol)',fontsize=fontsize_label)
#plt.savefig('condi_binding_prob.png',dpi=220)