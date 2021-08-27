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
def hot_start(n):
    spin = np.random.randint(0, 2, n)
    spin[spin == 0] = -1
    return spin
def all_zero_start(n):
    spin = np.full(n,-1)

    return spin

def flipkpi(tau,spin_temp, coeff):
    global n
    # print(" i is "+str(i)+" j is "+str(j))
    kpi_temp = 0
 
    for i in range(n):
        if(tau[i]!= spin_temp[i]):           
            kpi_temp = kpi_temp + 2*spin_temp[i]*coeff[i]
    return kpi_temp    


def firstupdate(spin,t1):
    
    global n,coeff
    spin_temp = np.copy(spin)
    tau = np.zeros(n)
    for i in range(n):
        
        kp = kpi(spin_temp, coeff[i])
        # kp = kpi(spin_temp, coeff[i])+ kp_prev1[i]
        kp_prev1[i] = kp
        # print(kp)
        current_spin = spin[i]
        temp =(current_spin*kp )/(2*t1)
        px = sigmoid(temp)
        rand = random.uniform(0, 1)
        # print("px is "+ str(px)+"rand is "+str(rand))
        if px < rand:
            tau[i] = -1 * current_spin
        else:
            tau[i] =  current_spin
     
    return tau
               

def update(spin,prev,t1):
     global q1,kp_prev1,n,coeff
     spin_temp = np.copy(spin)
     tau = np.zeros(n)
    
     for i in range(n):
        kp = flipkpi(prev,spin_temp, coeff[i])+ kp_prev1[i]
        # kp = kpi(spin_temp, coeff[i])+ kp_prev1[i]
        kp_prev1[i] = kp
        # print(kp)
        current_spin = spin[i]
        temp =(current_spin*kp )/(2*t1)
        px = sigmoid(temp)
        rand = random.uniform(0, 1)
        # print("px is "+ str(px)+"rand is "+str(rand))
        if px < rand:
            tau[i] = -1 * current_spin
        else:
            tau[i] =  current_spin
     
     return tau

def kpi(spin, coeff):
    global n
    # print(" i is "+str(i)+" j is "+str(j))
    kpi_temp = 0
 
    for i in range(n):
        kpi_temp = kpi_temp + spin[i]*coeff[i]
    return kpi_temp               


# def kpi(tau,spin,coeff):
#     global n
#     # print(" i is "+str(i)+" j is "+str(j))
#     kpi_temp = 0
 
#     for i in range(n):
#         if(tau[i]!= spin[i]):           
#             kpi_temp = kpi_temp + 2*spin[i]*coeff[i]
#     return kpi_temp        


n = 800





# for i in range(nx):
#     for j in range(ny):
#             temp = generate_random_coefficient(i,j,n)
#             tcoeff[i][j] =temp
# print(tcoeff)        
# coeff =  CoeffGen(n)
loaded_arr = np.loadtxt('G1coeff.txt')

coeff =  np.where(loaded_arr ==1,-1,0)
lastnumber =[]
pfnumber =[]
stot=560
q1 =3
tinit = 50
tfin =4
te = 1/(stot-1)
rq=1.0**(te)

t1 = tinit
rt = (tfin/tinit)**(te)
spin = all_zero_start(n)
out = np.zeros(stot)
temperature =[]
temperature.append(t1)
kp_prev1 = np.zeros(n)
tau = np.zeros(n)
prev_spin = np.zeros(n)
for s in range(1,stot):

    if s == 1:
        tau = firstupdate(spin, t1)
    else:    
        tau = update(spin,prev_spin,t1)
    t1 =  t1*rt
    temperature.append(t1)
    print(f"iteration = {s}")
    prev_spin= np.copy(spin)
    spin = np.copy(tau)
    for i in range(n):      
        out[s] = out[s] -(spin[i] * kpi(spin, coeff[i]))
                
    print(out[s])
minval = np.min(out)            
print(out)
print(out[-1])
print(minval)
lastnumber.append(out[-1])  
pfnumber.append(minval)



plt.plot(temperature)    
plt.figure(figsize=(10, 6))
plt.plot(out)
titl = '256 Spin fully connected tokyo  256 iteration ='+str(stot)
plt.title(titl, fontsize=18)
plt.xlabel('Iteration', fontsize=10)
plt.ylabel('out', fontsize=10)
plt.grid()
plt.show()
