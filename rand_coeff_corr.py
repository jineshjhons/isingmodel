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




pcoeff = generate_random_coefficient(nx)
temp = generate_random_coefficient(nx)
rcoeff = np.where(temp == 0,-1,temp)

# np.savetxt('icoeff.txt',newicoeff)
np.savetxt('rcoeff.txt',rcoeff)
np.savetxt('pcoeff.txt',pcoeff)
print(temp) 


