# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:20:29 2021

@author: JineshJhonsa
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# Set initial spins
def hot_start(x):
   
    spin = np.random.randint(0, 2, x)
    spin[spin == 0] = -1
   
    
    return spin


def manual_start(row,col):
    spin =[1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1]
    spin = np.reshape(spin,(row,col))
    return spin



def generate_linear_random(n,it):
    final =0
    y = it-final
    beta = 0.5
    step =1.25* 0.5/y
    rh = np.empty([it,n])
    rv = np.empty([it,n])
    for x in range(y):
        beta =beta +step
        hori = np.random.rand(n) -beta
        h = np.where(hori>0,1,-1)
        rh[x] =h 
        vert = np.random.rand(n) -(1-beta)
        v = np.where(vert>0,1,-1)
        rv[x] =v
    beta = 0.5
    step =1* 0.5/y    
    for x in range(y,it):
        beta =beta +step
        hori = np.random.rand(n) -beta
        h = np.where(hori>0,1,-1)
        rh[x] =h 
        vert = np.random.rand(n) -(1-beta)
        v = np.where(vert>0,1,-1)
        rv[x] =v
            
        
    return rh,rv
        

def kpi(spin, coeff):
    global n
    # print(" i is "+str(i)+" j is "+str(j))
    kpi_temp = 0
 
    for i in range(n):
        kpi_temp = kpi_temp + spin[i]*coeff[i]
    return kpi_temp        


def update1(spin,rh,rv):
    spin_pre = np.copy(spin)   
    for i in range(128):
        kp = kpi(spin_pre, coeff[i])
        w=50
        E =  kp + w*rh[i] + w*rv[i]    
        if E > 0:
            spin[i] = +1
        else:
            spin[i] = -1   
    return spin
def update2(spin,rh,rv):
    global w
    spin_pre = np.copy(spin)   
    for i in range(128,256):
        kp = kpi(spin_pre, coeff[i])
  
        E =  kp + w*rh[i] + w*rv[i]    
        if E > 0:
            spin[i] = +1
        else:
            spin[i] = -1   
    return spin
n = 800
w = 0
iteration = 100

beta = 0
step = 0.01
     
# coeff =  CoeffGen(n)
loaded_arr = np.loadtxt('G1coeff.txt')
coeff = loaded_arr
lastnumber =[]
pfnumber =[]
for z in range(1): 
    Rh, Rv = generate_linear_random(n,iteration)

    print(f"iteration = {z}")
    print(z)
    spin = hot_start(n)
    out = np.zeros(iteration)
    betadata =[]
    kp_prev =[]
    for k in range(iteration):
        print(k)
        ranh =Rh[k]
        ranv = Rv[k]
        if k%2 ==0:
            spin = update1(spin,ranh,ranv)
        else:
            spin = update2(spin,ranh,ranv)
        for i in range(n):
                     
            out[k] = out[k] -(1*spin[i] *kpi(spin, coeff[i]))
                
        print(out[k])
    minval = np.min(out)            
    print(out)
    print(out[-1])
    print(minval)
    lastnumber.append(out[-1])  
    pfnumber.append(minval)
    new_spin  = np.array(spin)
    titl = '256 Spin fully connected 128 update  W = '+str(w)+' iteration ='+str(iteration)
    plt.figure(figsize=(10, 6))
    plt.plot(out)
    plt.title(titl, fontsize=18)
    plt.xlabel('Iteration', fontsize=10)
    plt.ylabel('out', fontsize=10)
    plt.grid()
    plt.show()
    
    
    
    
