#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:33:07 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
def re_generate_m(flat_m):
    a = np.unique(flat_m[:,0])
    b = np.unique(flat_m[:,1])
    A,B = np.meshgrid(b,a)
    Z = np.zeros((len(a),len(b)))
    for i in range(len(a)):
        for j in range(len(b)):
            Z[i][j] = flat_m[i*len(b)+j][2]
    return A,B,Z
#data1 = np.loadtxt('E_L_2d.out')
#data = -np.log(np.where(data1<=0,1e-9,data1))
data = np.loadtxt('pmf2d_num_endct_num_sidect_300.dat')
fontsize_label = 18
fontsize_title = 18
fontsize_tick = 12
levels =  np.arange(0,13)
X,Y,Z = re_generate_m(data)
test = data[:,2].reshape(40,36)
#P = np.exp(-Z)/np.sum(np.exp(-Z))
#print (np.sum(P))
#print("@ E: ", np.sum(P[17:27,0])*100)
#print ("disa: ",(P[0,0]+P[0,1]+P[1,0])*100)
#print ("@ L: ", (np.sum(P[0,16:23])+np.sum(P[2,18:22]))*100)
'''
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
heatmap = plt.contourf(X,Y,Z,levels=levels,cmap='jet')#colors=Colors)
#heatmap = plt.contourf(data, extent=[y[0], y[-1], x[0], x[-1]],levels=levels)
plt.ylabel('No. residues contact elongation surface',fontsize=fontsize_label)
plt.xlabel('No. residues contact lateral surface',fontsize=fontsize_label)
plt.tick_params(labelsize=fontsize_tick)
cb = plt.colorbar(heatmap,fraction=0.02,pad=0.1)
'''
