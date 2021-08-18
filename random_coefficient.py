# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:49:42 2021

@author: JineshJhonsa
"""
import numpy as np

def generate_coefficient(image,i,j,n):
    arr =[]
    val = image[i][j]
    for x in range(n):
        for y in range(n):
            if x ==i and y ==j:
                arr.append(0)
            elif val == image[x][y]:
                arr.append(+1)
            else:
                arr.append(-1)
    return arr

def generate_random_coefficient(n):
    spin = np.random.randint(0, 2, n)
    spin[spin == 0] = -1
    
    return spin



def generate_pos_coefficient(n):
    spin = np.random.randint(0, 2, n)
    return spin

nx = 256
ny =256

ns = nx*ny
tcoeff = np.empty([nx,ny])
pcoeff = np.empty([nx,ny])
for i in range(nx):
    temp = generate_random_coefficient(nx)
    tcoeff[i] =temp
print(tcoeff) 
   

for i in range(nx):
    temp = generate_pos_coefficient(nx)
    pcoeff[i] =temp
print(pcoeff) 


image = np.loadtxt('./coeff8_16x16.csv', delimiter=',')
no = image.shape
nx1 = no[0]
ny1 = no[1]
icoeff = np.empty([nx1,ny1,nx])
for i in range(nx1):
    for j in range(ny1):
        temp = generate_coefficient(image,i,j,nx1)
        icoeff[i][j] =temp
newicoeff = icoeff.reshape((icoeff.shape[0]*icoeff.shape[1]),icoeff.shape[2])
        
np.savetxt('icoeff.txt',newicoeff)
np.savetxt('tcoeff.txt',tcoeff)
np.savetxt('pcoeff.txt',pcoeff)