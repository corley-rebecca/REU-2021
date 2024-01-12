#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 17:30:14 2021

@author: rebeccacorley
"""
"""
a plotting script that selects a certain surface 
area and then plots only the arrival direction of 
the photons for that area. This script is for a Gen2 geometry.
"""

#import required libraries 
import numpy as np
import matplotlib.pyplot as plt 



#read in data from CamSim simulation run, called 'data'
data = np.load('/Users/rebeccacorley/CamSim-Gen2/run_outputs/Hole_fS1O2_cS1O1_fOri0_fTil90_fWid20.5_fWav470_pNum11700000_T1628011141.3136508.npz')
print(data.files)
print(type(data))

print(np.shape((data['p_theta'])))
print(np.shape(data['d_phi']))


#empty array for values
d_theta_values = []
d_phi_values = []
#np.array[d_theta_values]


fig = plt.figure(figsize = (10, 5)) #assigns fig size


#for values in p_theta, cut specified range, the plot world coordinates (d_theta) in 2dhist
for i in range(np.shape(data['p_theta'])[0]):
    #print(i)
    if  (data['p_phi'][i] > 0.785398) and (data['p_phi'][i] < 2.35619) and (data['p_theta'][i] > 0.785398) and (data['p_theta'][i] < 0.785398):
        d_theta_values.append(data['d_theta'][i])
        d_phi_values.append(data['d_phi'][i])
       
        
plt.hist2d(d_phi_values, d_theta_values, bins=(50, 50), cmap=plt.cm.viridis)
plt.colorbar().set_label('counts in bin')
plt.clim(0,4) #set range of colorbar
plt.xlim(-3,3)
plt.ylim(0,3)
plt.xlabel('Arrivial $\phi$ [rad]', fontsize = 18)
plt.ylabel('Arrivial $\Theta$ [rad]', fontsize = 18)
#plt.savefig('test_plot.pdf'.format(i))


