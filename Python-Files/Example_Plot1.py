#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:24:17 2021

@author: rebeccacorley
"""
import numpy as np
import matplotlib.pyplot as plt 




data = np.load('/Users/rebeccacorley/CamSim-Gen2/run_outputs/Upgrade_fS87O50_cS93O54_fOri0_fTil0_fWid20.5_fWav470_pNum11700000_T1627435599.582307.npz')

print(data)
fig = plt.figure(figsize = (10, 5))


plt.hist2d(data['p_phi'], data['p_theta'], bins=(50), cmap=plt.cm.viridis)
plt.colorbar()
plt.clim(0,3000)
plt.xlim(-3,3)
plt.ylim(0,3)
plt.xlabel('Arrivial $\phi$ [rad]', fontsize = 18)
plt.ylabel('Arrivial $\Theta$ [rad]', fontsize = 18)
plt.show()

