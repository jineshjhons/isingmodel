# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:23:36 2021

@author: JineshJhonsa
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import random


def sigmoid(x):
  return 1 / (1 + math.exp(-x))
def hot_start(x,y):
    global ns
    spin = np.random.randint(0, 2, ns)
    spin[spin == 0] = -1
    spin = np.reshape(spin,(x,y))
    
    return spin

def update(spin,t1):
    global q1,kp_prev1
    spin_pre = np.copy(spin)
  
    
    for i in range(n):
        for j in range(n):
            
            
            kp = kpi(spin_pre, coeff[i][j])+ kp_prev1[i][j]
            kp_prev1[i][j] = kp
            # print(kp)
            current_spin = spin[i][j]
            temp =(current_spin*kp )/(2*t1)
            px = sigmoid(temp)
            rand = random.uniform(0, 1)
            print("px is "+ str(px)+"rand is "+str(rand))
            if px < rand:
                spin[i][j] = -1 * current_spin
             
    return spin

def kpi(spin, coeff):
    global n
    # print(" i is "+str(i)+" j is "+str(j))
    kpi_temp = 0
 
    for i in range(n):
        for j in range(n):
            ind = i*n+j
            kpi_temp = kpi_temp + spin[i][j]*coeff[ind]
    return kpi_temp        


n = 16
ns = n*n

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
loaded_arr = np.loadtxt('rcoeff.txt')
tcoeff =loaded_arr.reshape((16,16,256))
coeff = tcoeff
lastnumber =[]
pfnumber =[]
stot=560
q1 =3
tinit = 50
tfin =4
te = 1/(stot-1)
rq=1.0**(te)
N=256
t1 = tinit
rt = (tfin/tinit)**(te)
spin = hot_start(n,n)
out = np.zeros(stot)
temperature =[]
temperature.append(t1)
kp_prev1 = np.zeros([n,n])
for s in range(1,stot):
     spin = update(spin,t1)
     t1 =  t1*rt
     temperature.append(t1)
     print(f"iteration = {s}")
     for i in range(n):
            for j in range(n): 
            
                out[s] = out[s] -(1*spin[i][j] *kpi(spin, coeff[i][j]))
                
     print(out[s])
minval = np.min(out)            
print(out)
print(out[-1])
print(minval)
lastnumber.append(out[-1])  
pfnumber.append(minval)
new_spin  = np.array(spin)
spin_2d = np.reshape(new_spin,(n,n))   
plt.plot(temperature)    
plt.figure(figsize=(10, 6))
plt.plot(out)
plt.title('16x16 Spin2 by CPU', fontsize=18)
plt.xlabel('Iteration', fontsize=10)
plt.ylabel('out', fontsize=10)
plt.grid()
plt.show()
