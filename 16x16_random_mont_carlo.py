# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:20:29 2021

@author: JineshJhonsa
"""

import math
import numpy as np
import matplotlib.pyplot as plt

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

           
def north(image,i,j):
    if i-1<0:
        return 0
    if image[i][j] == image[i-1][j]:
        return 1
    return -1

def northeast(image,i,j):
    x = image.shape
    nrow = x[0]
    ncol = x[1]
    if i-1<0 or j+1>=ncol:
        return 0
    if image[i][j] == image[i-1][j+1]:
        return 1
    return -1
def east(image,i,j):
    x = image.shape
    nrow = x[0]
    ncol = x[1]
    if j+1>=ncol:
        return 0
    if image[i][j] == image[i][j+1]:
        return 1
    return -1

def southeast(image,i,j):
    x = image.shape
    nrow = x[0]
    ncol = x[1]
    if i+1>=nrow or j+1>=ncol:
        return 0
    if image[i][j] == image[i+1][j+1]:
        return 1
    return -1

def south(image,i,j):
    x = image.shape
    nrow = x[0]
    ncol = x[1]
    if i+1>=nrow:
        return 0
    if image[i][j] == image[i+1][j]:
        return 1
    return -1

def southwest(image,i,j):
    x = image.shape
    nrow = x[0]
    ncol = x[1]
    if i+1>=nrow or j-1<0:
        return 0
    if image[i][j] == image[i+1][j-1]:
        return 1
    return -1

def west(image,i,j):
    x = image.shape
    nrow = x[0]
    ncol = x[1]
    if j-1<0:
        return 0
    if image[i][j] == image[i][j-1]:
        return 1
    return -1

def northwest(image,i,j):
    x = image.shape
    nrow = x[0]
    ncol = x[1]
    if i-1<0 or j-1<0:
        return 0
    if image[i][j] == image[i-1][j-1]:
        return 1
    return -1



def array(image,i,j):
   
    arr =[]
    arr.append(north(image,i,j))
    arr.append(northeast(image,i,j))
    arr.append(east(image,i,j))
    arr.append(southeast(image,i,j))
    arr.append(south(image,i,j))
    arr.append(southwest(image,i,j))    
    arr.append(west(image,i,j))
    arr.append(northwest(image,i,j))
    return arr



def generate_linear_random(n):
    beta = 0.5
    step = 0.5/1000
    rh = np.empty([1000,n])
    rv = np.empty([1000,n])
    for x in range(1000):
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
def kpi(spin, coeff, i,j):
    
    # print(" i is "+str(i)+" j is "+str(j))
    kpi_temp = 0
    for k in range(8):
        if coeff[k] != 0:
            if k == 0:
                kpi_temp = kpi_temp + coeff[k] * spin[i-1][j]
            elif k == 1:
                kpi_temp = kpi_temp + coeff[k] * spin[i-1][j+1]
            elif k == 2:
                kpi_temp = kpi_temp + coeff[k] * spin[i][j+1]
            elif k == 3:
                kpi_temp = kpi_temp + coeff[k] * spin[i+1][j+1]
            elif k == 4:
                kpi_temp = kpi_temp + coeff[k] * spin[i+1][j]
            elif k == 5:
                kpi_temp = kpi_temp + coeff[k] * spin[i+1][j-1]
            elif k == 6:
                kpi_temp = kpi_temp + coeff[k]  * spin[i][j-1]
            elif k == 7:
                kpi_temp = kpi_temp + coeff[k]  * spin[i-1][j-1]
            

       
    # 
    return kpi_temp

# The main Monte Carlo Loop

# beta represents 1/kT
# i is row and j is column
def update(spin,rh,rv):
    global kp_prev1,kp_prev2
    spin_pre = np.copy(spin)
    kp_prev =0
    
    for i in range(n):
        for j in range(n):
            
            rval = i%4
            kp = kpi(spin_pre, coeff[i][j], i,j)
            print(kp)
            kp1 = kp - kp_prev1[i][j] 
            
            kp_prev1[i][j] = kp
            w=8
            E =  -kp1 + w*rh[rval] + w*rv[rval]    
            if E > 0:
                spin[i][j] = +1
            else:
                spin[i][j] = -1   
    return spin
n = 16
ns = n*n
iteration = 1000
beta = 0
step = 0.01
Rh, Rv = generate_linear_random(n)       
image = np.loadtxt('./coeff8_16x16.csv', delimiter=',')
no = image.shape
nx = no[0]
ny = no[1]
tcoeff = np.empty([nx,ny,8])
kp_prev1 = np.zeros([n,n])
kp_prev2 = np.zeros([n,n])


        
for i in range(nx):
    for j in range(ny):
        temp = array(image,i,j)
        tcoeff[i][j] =temp
print(tcoeff)        
coeff =  np.array(tcoeff)




print(f"Size = {n}")
print(f"iteration = {iteration}")
spin = hot_start(n,n)
out = np.zeros(iteration)
betadata =[]
kp_prev =[]
for k in range(iteration):
    ranh =Rh[k]
    ranv = Rv[k]
    spin = update(spin,ranh,ranv)
    spin_temp = np.reshape(spin,(n,n))       
    for i in range(n):
        for j in range(n):            
            rval = j%4
            out[k] = out[k] -(1*spin[i][j] *kpi(spin, coeff[i][j],i,j))
            
            # print(out[k])
            
print(out)
print(np.min(out))
new_spin  = np.array(spin)
spin_2d = np.reshape(new_spin,(n,n))       
plt.figure(figsize=(10, 6))
plt.plot(out)
plt.title('16x16 Spin2 by CPU', fontsize=18)
plt.xlabel('Iteration', fontsize=10)
plt.ylabel('out', fontsize=10)
plt.grid()
plt.show()




