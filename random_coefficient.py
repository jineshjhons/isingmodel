# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:49:42 2021

@author: JineshJhonsa
"""
import numpy as np

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


np.savetxt('tcoeff.txt',tcoeff)
np.savetxt('pcoeff.txt',pcoeff)