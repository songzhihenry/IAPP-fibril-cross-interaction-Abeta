#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:23:18 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt

fontsize_label = 18
fontsize_title = 18
fontsize_tick = 12
mask_ctrl = np.loadtxt('../../dimer/replica_Ab/condi/ave_mask.dat')[:,1]
mask_side = np.loadtxt('./side/ave_mask.dat')[:,1]
mask_end = np.loadtxt('./end/ave_mask.dat')[:,1]
ctrl = np.loadtxt('../../dimer/replica_Ab/condi/ave_rg.dat').T
side = np.loadtxt('./side/ave_rg.dat').T
end = np.loadtxt('./end/ave_rg.dat').T
mask = [mask_end,mask_side,mask_ctrl]
data = [end, side, ctrl]
plt.figure(figsize=(12,5))
label = ['@ E fib','@ L fib','- fib']
for i in range(3):
    temp = data[i][0]
    cv = data[i][1]/mask[i]
    err = data[i][2]
    plt.plot(temp,cv,label=label[i])
    plt.errorbar(temp,cv,yerr=(err/24)**0.5,fmt='none',capsize=1,ecolor='lightgrey')
plt.legend(frameon=False,fontsize=fontsize_label)
plt.xlabel('temperature (K)',fontsize=fontsize_label)
plt.ylabel('rg (Å)',fontsize=fontsize_label)
plt.savefig('condi_rg.png',dpi=220)