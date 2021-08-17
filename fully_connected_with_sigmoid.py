# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:34:17 2021

@author: JineshJhonsa
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:20:29 2021

@author: JineshJhonsa
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import random
def sigmoid(x):
  return 1 / (1 + math.exp(-x))
# Set initial spins
def hot_start(x,y):
    global ns
    spin = np.random.randint(0, 2, ns)
    spin[spin == 0] = -1
    spin = np.reshape(spin,(x,y))
    
    return spin


def manual_start(row,col):
    spin =[1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1]
    spin = np.reshape(spin,(row,col))
    return spin
# Measure magnetization
def mag(spin):
    global ns
    m = 0
    for i in range(ns):
        m = m + spin[i]
    return m

# Calculate KPI

     
# Main

# coeff = np.loadtxt('./coeff8_4x4_1_t.csv', delimiter=',')

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


def generate_random_coefficient(i,j,n):

    ns = n*n
    spin = np.random.randint(0, 2, ns)
    spin[spin == 0] = -1
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
        
def generate_random(n):
   anneal = 100
   is_anneal =400
   ising =500
   rh = np.empty([500,n],dtype = int)
   rv = np.empty([500,n],dtype = int)
   
   for x in range(anneal):
       
       rh[x] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
       rv[x] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
       # if x %100 ==0:
       #     rh[x] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
       #     rv[x] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
       # else:  
       #     rh[x] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
       #     rv[x] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

   for y in range(anneal,is_anneal):
       rh_rand = np.random.randint(2, size=n)
       rv_rand = np.random.randint(2, size=n)
       rh[y] = np.where(rh_rand == 0, -1, rh_rand)
       rv[y] = np.where(rv_rand == 0, -1, rv_rand)
   for z in range(is_anneal,ising):
       
        rh[z] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        rv[z] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
       
         
   return rh,rv   
def kpi(spin, coeff):
    global n
    # print(" i is "+str(i)+" j is "+str(j))
    kpi_temp = 0
    y = len(coeff)
    for i in range(n):
        for j in range(n):
            ind = i*n+j
            kpi_temp = kpi_temp + spin[i][j]*coeff[ind]
    return kpi_temp        



def update(spin,rh,rv):
    global kp_prev1,kp_prev2
    spin_pre = np.copy(spin)
    kp_prev =0
    
    for i in range(n):
        for j in range(n):
            
            rval = i%n
            kp = kpi(spin_pre, coeff[i][j])
            # print(kp)
            # kp1 = kp - kp_prev1[i][j] 
            
            # kp_prev1[i][j] = kp
            w=100
            current_spin = spin[i][j]
            E =  kp + w*rh[i] + w*rv[j]  
            
            px = sigmoid(E*current_spin)
            rand = random.uniform(0, 1)
            print("px is "+ str(px)+"rand is "+str(rand))
            if px < rand:
                spin[i][j] = -1 *  current_spin
    return spin
n = 16
ns = n*n
iteration = 1500   

beta = 0
step = 0.01
image = np.loadtxt('./coeff8_16x16.csv', delimiter=',')
no = image.shape
nx = no[0]
ny = no[1]
tcoeff = np.empty([nx,ny,ns])
# for i in range(nx):
#     for j in range(ny):
#             temp = generate_random_coefficient(i,j,n)
#             tcoeff[i][j] =temp
# print(tcoeff)        
# coeff =  CoeffGen(n)
loaded_arr = np.loadtxt('tcoeff.txt')
tcoeff =loaded_arr.reshape((16,16,256))
coeff = tcoeff
lastnumber =[]
pfnumber =[]
for z in range(1): 
    Rh, Rv = generate_linear_random(n,iteration)       
    kp_prev1 = np.zeros([n,n])
    kp_prev2 = np.zeros([n,n])
    

    print(f"iteration = {z}")
    print(z)
    spin = hot_start(n,n)
    out = np.zeros(iteration)
    betadata =[]
    kp_prev =[]
    for k in range(iteration):
        print(k)
        ranh =Rh[k]
        ranv = Rv[k]
        spin = update(spin,ranh,ranv)
        spin_temp = np.reshape(spin,(n,n))       
        for i in range(n):
            for j in range(n):            
                out[k] = out[k] -(1*spin[i][j] *kpi(spin, coeff[i][j]))
                
                # print(out[k])
    minval = np.min(out)            
    print(out)
    print(out[-1])
    print(minval)
    lastnumber.append(out[-1])  
    pfnumber.append(minval)
    new_spin  = np.array(spin)
    spin_2d = np.reshape(new_spin,(n,n))       
    plt.figure(figsize=(10, 6))
    plt.plot(out)
    plt.title('16x16 Spin2 by CPU', fontsize=18)
    plt.xlabel('Iteration', fontsize=10)
    plt.ylabel('out', fontsize=10)
    plt.grid()
    plt.show()
    
    
    
    
