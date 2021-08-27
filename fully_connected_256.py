# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:20:29 2021

@author: JineshJhonsa
"""

import math
import numpy as np
import matplotlib.pyplot as plt
def all_zero_start(n):
    spin = np.full(n,-1)

    return spin
# Set initial spins
def hot_start(x):
   
    spin = np.random.randint(0, 2, x)
    spin[spin == 0] = -1
   
    
    return spin




# Calculate KPI

     
# Main

# coeff = np.loadtxt('./coeff8_4x4_1_t.csv', delimiter=',')





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



def update(spin,rh,rv):
    global w
    spin_pre = np.copy(spin)   
    for i in range(n):
        kp = kpi(spin_pre, coeff[i])
        
        E =  kp + w*rh[i] + w*rv[i]    
        if E > 0:
            spin[i] = +1
        else:
            spin[i] = -1   
    return spin

n = 800
w =3
iteration = 1200

beta = 0
step = 0.01
     
# coeff =  CoeffGen(n)
loaded_arr = np.loadtxt('G1coeff.txt')

coeff = np.where(loaded_arr ==1,-1,0)
lastnumber =[]
pfnumber =[]
for z in range(1): 
    Rh, Rv = generate_linear_random(n,iteration)
    

    # print(f"iteration = {z}")
    print(z)
    spin = all_zero_start(n)
    out = np.zeros(iteration)
    betadata =[]
    kp_prev =[]
    for k in range(iteration):
        print(k)
        ranh =Rh[k]
        ranv = Rv[k]
        spin = update(spin,ranh,ranv)
    
        for i in range(n):
        
            out[k] = out[k] -(1*spin[i] *kpi(spin, coeff[i]))
                
                # print(out[k])
    minval = np.min(out)            
    print(out)
    print(out[-1])
    print(minval)
    lastnumber.append(out[-1])  
    pfnumber.append(minval)
    new_spin  = np.array(spin)
    titl = '256 Spin fully connected  update  W = '+str(w)+' iteration ='+str(iteration)
    plt.figure(figsize=(10, 6))
    plt.plot(out)
    plt.title(titl, fontsize=18)
    plt.xlabel('Iteration', fontsize=10)
    plt.ylabel('out', fontsize=10)
    plt.grid()
    plt.show()
    
    
    
    
