# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:37:41 2021

@author: JineshJhonsa
"""
import numpy as np
def generate_random_coefficient(n):
    tcoeff = np.full((n,n),5)
    spin = []
    # for i in range(n):
    #     x = np.random.randint(0, 2, n)
    #     spin[i] = x
    # tcoeff[0] = spin
    for i in range(n):
        for j in range(n):
            if(j<i):
                tcoeff[i][j] = tcoeff[j][i]
            else:
                tcoeff[i][j] = np.random.randint(0, 2)
            
    return tcoeff

nx =256

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
pcoeff = generate_random_coefficient(nx)
temp = generate_random_coefficient(nx)
rcoeff = np.where(temp == 0,-1,temp)

# np.savetxt('icoeff.txt',newicoeff)
np.savetxt('rcoeff.txt',rcoeff)
np.savetxt('pcoeff.txt',pcoeff)
print(temp) 


