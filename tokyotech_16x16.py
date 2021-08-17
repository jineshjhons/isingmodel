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

def randomarray():
    arr =[]
    for j in range(8):
        
        spin = np.random.randint(0, 2, ns)
        arr.append(spin)
    arr[spin] =1
    

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
       
def RndGen(n, iteration):
    x = int(iteration / 5)
    rnd = np.random.rand(iteration)
    for i in range(x):
        if rnd[i] > 0.5:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(x, 2*x):
        if rnd[i] > 0.8:
            rnd[i] = 0
        elif rnd[i] <= 0.8 and rnd[i] > 0.4:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(2*x, 3*x):
        if rnd[i] > 0.6:
            rnd[i] = 0
        elif rnd[i] <= 0.6 and rnd[i] > 0.3:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(3*x, 4*x):
        if rnd[i] > 0.2:
            rnd[i] = 0
        elif rnd[i] <= 0.2 and rnd[i] > 0.1:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(4*x, iteration):
        rnd[i] = 0
    
    return rnd 

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
def update1(spin,rh,rv):
    global kp_prev1,kp_prev2
    spin_pre = np.copy(spin)
    kp_prev =0
    
    for i in range(n):
        for j in range(n):
            if i %2 ==0 and j%2 ==0:
                rval = i%4
                kp = kpi(spin_pre, coeff[i][j], i,j)
               
                w=1
                E =  kp + w*rh[rval] + w*rv[rval]    
                if E > 0:
                    spin[i][j] = +1
                else:
                    spin[i][j] = -1   
    return spin
def update2(spin,rh,rv):
    global kp_prev1,kp_prev2
    spin_pre = np.copy(spin)
    kp_prev =0
    
    for i in range(n):
        for j in range(n):
            if i %2 ==0 and j%2 ==1:
                rval = i%4
                kp = kpi(spin_pre, coeff[i][j], i,j)
               
                w=1
                E =  kp + w*rh[rval] + w*rv[rval]    
                if E > 0:
                    spin[i][j] = +1
                else:
                    spin[i][j] = -1   
    return spin
def update3(spin,rh,rv):
    global kp_prev1,kp_prev2
    spin_pre = np.copy(spin)
    kp_prev =0
    
    for i in range(n):
        for j in range(n):
            if i %2 ==1 and j%2 ==0:
                rval = i%4
                kp = kpi(spin_pre, coeff[i][j], i,j)
               
                w=1
                E =  kp + w*rh[rval] + w*rv[rval]    
                if E > 0:
                    spin[i][j] = +1
                else:
                    spin[i][j] = -1   
    return spin
def update4(spin,rh,rv):
    global kp_prev1,kp_prev2
    spin_pre = np.copy(spin)
    kp_prev =0
    
    for i in range(n):
        for j in range(n):
            if i %2 ==1 and j%2 ==1:
                rval = i%4
                kp = kpi(spin_pre, coeff[i][j], i,j)
               
                w=1
                E =  kp + w*rh[rval] + w*rv[rval]    
                if E > 0:
                    spin[i][j] = +1
                else:
                    spin[i][j] = -1   
    return spin


def latticeneg(n):
    coeff = np.zeros([n*n, 8])
    for i in range(n):
        for j in range(n):
            coeff[i*n+j,0] = -1
            coeff[i*n+j,2] = -1
            coeff[i*n+j,4] = -1
            coeff[i*n+j,6] = -1
    return coeff

def setzero(n, coeff):
    for i in range(n):
        for j in range(n):
            if i == 0:
                coeff[i*n+j,0] = 0
                coeff[i*n+j,1] = 0
            if j == n-1:
                coeff[i*n+j,1] = 0
                coeff[i*n+j,2] = 0
                coeff[i*n+j,3] = 0
            if i == n-1:
                coeff[i*n+j,3] = 0
    return coeff

def Four2Eight(n, coeff_row):
    ns = n*n
    coeff = np.zeros([ns, 8])
    for i in range(ns):
        coeff[i, 0] = coeff_row[i, 0]
        coeff[i, 1] = coeff_row[i, 1]
        coeff[i, 2] = coeff_row[i, 2]
        coeff[i, 3] = coeff_row[i, 3]
        if i >= n*(n-1):
            coeff[i, 4] = 0
        else:
            coeff[i, 4] = coeff_row[i+n, 0]
        if i % n == 0 or i >= n*(n-1):
            coeff[i, 5] = 0
        else:
            coeff[i, 5] = coeff_row[i-5, 1]
        if i % n == 0:
            coeff[i, 6] = 0
        else:
            coeff[i, 6] = coeff_row[i-1, 2]
        if i < n or i % n == 0:
            coeff[i, 7] = 0
        else:
            coeff[i, 7] = coeff_row[i-7, 3]

    return coeff

def CoeffGen(n):
    # coeff = np.random.randint(3, size = (n*n, 4))
    # coeff[coeff==2] = -1
    coeff = latticeneg(n)
    coeff = setzero(n, coeff)
    coeff = Four2Eight(n, coeff)
    temp = np.reshape(coeff,(n,n,8))
    return temp
n = 16
ns = n*n
iteration = 1000

        
image = np.loadtxt('./coeff8_16x16.csv', delimiter=',')
no = image.shape
nx = no[0]
ny = no[1]
tcoeff = np.empty([nx,ny,8])
kp_prev1 = np.zeros([n,n])
kp_prev2 = np.zeros([n,n])

pfnumber = []
lastnumber =[]        
for i in range(nx):
    for j in range(ny):
        temp = array(image,i,j)
        tcoeff[i][j] =temp
print(tcoeff)        
coeff =  CoeffGen(n)
   
       
for z in range(5):    
    print(f"Size = {n}")
    
    
    print(f"iteration number = ")
    print(z)
    Rh,Rv = generate_linear_random(n,iteration)   
    spin = hot_start(n,n)
    out = np.zeros(iteration)
    betadata =[]
    kp_prev =[]
    for k in range(iteration):
        
        ranh =Rh[k]
        ranv = Rv[k]
        spin = update1(spin,ranh,ranv)
        spin = update2(spin,ranh,ranv)
        spin = update3(spin,ranh,ranv)
        spin = update4(spin,ranh,ranv)
        spin_temp = np.reshape(spin,(n,n))       
        for i in range(n):
            for j in range(n):            
                rval = j%4
                out[k] = out[k] -(1*spin[i][j] *kpi(spin, coeff[i][j],i,j))
                
                # print(out[k])
                
    print(out)
   
    minval = np.min(out)
    print(minval)
    # np.savetxt(out'coeff8_16x16.csv',out, delimiter=',')
    
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
    



