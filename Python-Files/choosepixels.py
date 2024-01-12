#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:37:09 2021

@author: torisnyder
"""
#import numpy as np 
#data = np.loadtxt('/users/torisnyder/Downloads/img16.txt', unpack = 'False')
'''
For today, I think it will be most important to complete your script that selects a specific region of the image and obtains the pixel counts there, you need to separately treat red, green and blue pixels. Also you need to think about a way how you can ensure the user selected the right region of the image where the user wanted to obtain the pixel counts, otherwise with no feedback, one can easily introduce unintended mistakes.
'''

#if the readout value is above a certain number, then there is an object of interest 
#have user input a certain nxn number of pixels to indicate where they want to get pixel counts 

#first figure out how to get user to choose certain region.
#then get rgb values of that region
#making sure the user picked the right area of the picture:
    #do not run if readout value is below a certain number 
    #(because there is nothing of interest in that area)
   
import skimage.io
import skimage.viewer

image = skimage.io.imread(fname='darkimg.png')
viewer = skimage.viewer.ImageViewer(image)
viewer.show() 
clip = image[100:500, 300:800, :]
viewer = skimage.viewer.ImageViewer(clip)
viewer.show()
skimage.io.imsave(fname="clip.png", arr=clip)


'''
#crop image to whatever user wants 
from PIL import Image
im = Image.open('/Users/torisnyder/Desktop/icecube/pic.png')
width, height = im.size
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
im1 = im.crop((left,top,right,bottom))
im1.show()
im1.save('croppedim.png')
#get readouts and plot them 
image = Image.open('croppedim.png')


#get color values 
def get_color(self,x,y):

        if x % 2 == 0:

            if y % 2 == 0:

                return("red")

            else:

                return("green")

        elif y % 2 == 0:

            return("green")

        else:

            return("blue")
#for pixel in image: 
    #get_color(pixel)
'''