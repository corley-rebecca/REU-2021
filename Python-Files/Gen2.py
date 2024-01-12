#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:42:12 2021

@author: rebeccacorley
"""
"""
a plotting script that selects a certain surface 
area and then plots only the arrival direction of 
the photons for that area. It converts DOM to World coordinates. 
This script is for IceCube Gen2 geometry.
"""

#import required libraries 
import numpy as np
import matplotlib.pyplot as plt 
import time

start_time = time.time()


#read in data from CamSim simulation run, called 'data'
data = np.load('/Users/rebeccacorley/Gen2/run_outputs/Hole_fS1O2_cS1O1_fOri0_fTil90_fWid25.5_fWav470_pNum11700000_T1628012614.051559.npz')
print(data.files)
print(type(data))

print(np.shape((data['p_theta'])))
print(np.shape(data['d_phi']))


p_theta_world = []
p_phi_world = []


'''
loop through each of the p_theta/phi values in DOM coordinates
convert from DOM to world coordinates
'''
for i in range(np.shape(data['p_theta'])[0]):
    
    data['p_theta'][i] = np.pi - data['p_theta'][i]
    p_theta_world.append(data['p_theta'][i])
    
    if data['p_phi'][i] >= 0:
        
        x =  data['p_phi'][i] - np.pi
        p_phi_world.append(x)
        
    elif data['p_phi'][i] < 0:
        
        x = np.pi + data['p_phi'][i]
        p_phi_world.append(x)
         
        
#plot as a 2dhist in world coordinates       
plt.hist2d(p_phi_world, p_theta_world, bins=(1312, 979), cmap=plt.cm.viridis, rasterized = True)
#rasterized = True in your plot commands helps computation time and how long it takes the figure to load
plt.colorbar().set_label('counts in bin')
#plt.clim(0,4) #set range of colorbar
plt.xlim(-3,3)
plt.ylim(0,1)
plt.xlabel('Arrivial $\phi$ [rad]', fontsize = 18)
plt.ylabel('Arrivial $\Theta$ [rad]', fontsize = 18)   
plt.show()




  