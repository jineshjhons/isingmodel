import math
import numpy as np
import matplotlib.pyplot as plt

# Set initial spins
def hot_start():
    global ns
    spin = np.random.randint(0, 2, ns)
    spin[spin == 0] = -1

    return spin


def manual_start():
    spin =[1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,-1,-1]
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

def generate_random():
   anneal = 30 
   is_anneal =100
   ising =200
   rh = np.empty([200,4],dtype = int)
   rv = np.empty([200,4],dtype = int)
   for x in range(anneal):
       if x %2 ==0:
           rh[x] = [1,-1,1,-1]
           rv[x] = [-1,1,-1,1]
       else:
           rh[x] = [-1,1,-1,1]
           rv[x] = [1,-1,1,-1]

   for y in range(anneal,is_anneal):
       rh_rand = np.random.randint(2, size=4)
       rv_rand = np.random.randint(2, size=4)
       rh[y] = np.where(rh_rand == 0, -1, rh_rand)
       rv[y] = np.where(rv_rand == 0, -1, rv_rand)
   for z in range(is_anneal,ising):
       
        rh[z] = [-1,-1,-1,-1]
        rv[z] = [1,1,1,1]
       
         
   return rh,rv   
def kpi(spin, coeff, N):
    global n, ns
  
    kpi_temp = 0
    for i in range(8):
        if coeff[N, i] != 0:
            if i == 0:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N-n]
            elif i == 1:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N-n+1]
            elif i == 2:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+1]
            elif i == 3:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+n+1]
            elif i == 4:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+n]
            elif i == 5:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+n-1]
            elif i == 6:
                kpi_temp = kpi_temp + coeff[N, i]  * spin[N-1]
            elif i == 7:
                kpi_temp = kpi_temp + coeff[N, i]  * spin[N-n-1]
            

       
    # 
    return kpi_temp

# The main Monte Carlo Loop

# beta represents 1/kT
def update(rh,rv):
    global n, ns,spin
    
    for i in range(ns):
        rval = i%4
        kp = kpi(spin, coeff, i)
        w=3
        E =  kp + w*rh[rval] + w*rv[rval]    
        if E > 0:
            spin[i] = +1
        else:
            spin[i] = -1      
Rh, Rv = generate_random()       
image = np.loadtxt('./coeff8_4x4_2_t.csv', delimiter=',')
n = image.shape
nx = n[0]
ny = n[1]
tcoeff =[]

    

        
for i in range(nx):
    for j in range(ny):
        print(" i is "+str(i)+" j is "+str(j))

        temp = array(image,i,j)
        tcoeff.append(temp)
print(tcoeff)        
coeff =  np.array(tcoeff)


n = 4
ns = n*n
iteration = 200
beta = 0
step = 0.01

print(f"Size = {n}")
print(f"iteration = {iteration}")
spin = manual_start()
out = np.zeros(iteration)
betadata =[]

for i in range(iteration):
    ranh =Rh[i]
    ranv = Rv[i]
    update(ranh,ranv)
    spin_temp = np.reshape(spin,(4,4))       
    for j in range(ns):
        rval = j%4
        out[i] = out[i] -(1*spin[j] *kpi(spin, coeff, j))
        
print(out)

new_spin  = np.array(spin)
spin_2d = np.reshape(new_spin,(4,4))       
plt.figure(figsize=(10, 6))
plt.plot(out)
plt.title('4x4 Spin2 by CPU, GM = -33', fontsize=18)
plt.xlabel('Iteration', fontsize=10)
plt.ylabel('out', fontsize=10)
plt.grid()
plt.show()




