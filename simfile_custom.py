# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:16:31 2021

@author: JineshJhonsa
"""
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

data = np.zeros([100, 2], dtype = float)
wbll = open('new_write_bitline_left_coeff_256.txt', 'w')
wblr =  open('new_write_bitline_right_coeff_256.txt', 'w')
wwl  = open('new_write_word_coeff_256.txt', 'w')
init_dff = open('new_init_word_coeff_256.txt','w')
toffset = 0.000000001
tr = 0.02 # in nano seconds
wb = openpyxl.load_workbook("coeff_file.xlsx")
ind =0
i = 0
vdd=0.8
coe =[]
coeff =  wb['coeff']
x =0


for r in coeff.iter_rows():
    x = r[0].value
    coe.append(x)
    

def add_data(x,vdd):
    global ind,data,toffset
    ind = ind +1
    test = '{0:.12f}'.format(x*toffset)
    data[ind] =[test,vdd]
    
def add_coeff(coe,x):
    global toffset
    
    if coe == 1:
         wbll.write('%s %s \\\n' % ('{0:.12f}'.format((x)*toffset), '{0:.12f}'.format(vdd)))
         wblr.write('%s %s \\\n' % ('{0:.12f}'.format((x)*toffset), '{0:.12f}'.format(0)))
    if coe == -1:
         wbll.write('%s %s \\\n' % ('{0:.12f}'.format((x)*toffset), '{0:.12f}'.format(0)))
         wblr.write('%s %s \\\n' % ('{0:.12f}'.format((x)*toffset), '{0:.12f}'.format(vdd)))
    if coe == 0:
         wbll.write('%s %s \\\n' % ('{0:.12f}'.format((x)*toffset), '{0:.12f}'.format(0)))
         wblr.write('%s %s \\\n' % ('{0:.12f}'.format((x)*toffset), '{0:.12f}'.format(0)))


def initialize_word_bit_line_pulsewidth():
    wwl.write('simulator lang=spectre\n')
    wbll.write('simulator lang=spectre\n')
    wblr.write('simulator lang=spectre\n')
    init_dff.write('simulator lang=spectre\n')
    
    wwl.write('va3 (a\\<3\\> VSS) vsource dc=0 \n')
    wwl.write('va2 (a\\<2\\> VSS) vsource dc=0 \n')
    wwl.write('va1 (a\\<1\\> VSS) vsource dc=0 \n')
    wwl.write('va0 (a\\<0\\> VSS) vsource dc=0.8 \n')
    wbll.write('vwbl_0 (WBLL\\<0\\> VSS) vsource type=pwl wave=[  \\\n')
    wblr.write('vwrl_0 (WBLR\\<0\\> VSS) vsource type=pwl wave=[  \\\n') 
       


def sram_storage(dat):
    
    i =0 
    for x in dat:
       
        num = str(i)
        if x == 1:
            init_dff.write('vsram_'+ num +' (INIT\\<'+num+'\\> VSS) vsource dc=0.8 \n')
        else:
            init_dff.write('vsram_'+ num +' (INIT\\<'+num+'\\> VSS) vsource dc=0 \n')
        i =i +1
            

def activate_write_word_line(num,offset):
    global tr,coe
    x =0
    wwl.write('vwwl_%s (WWL\\<%s\\> VSS) vsource type=pwl wave=[  \\\n'%(num, num))  
    
    for i in range (offset):
        wwl.write('%s %s \\\n' % ('{0:.12f}'.format((i)*toffset), '{0:.12f}'.format(0)))
    
    wwl.write('%s %s \\\n' % ('{0:.12f}'.format((offset-1+tr)*toffset), '{0:.12f}'.format(vdd)))   
    for i in range(pwidth):
        x = i +offset 
        wwl.write('%s %s \\\n' % ('{0:.12f}'.format((x)*toffset), '{0:.12f}'.format(vdd)))
        if i ==0:
            add_coeff(coe[num],x+tr)
        else:
            add_coeff(coe[num],x)
            
    wwl.write('%s %s \\\n' % ('{0:.12f}'.format((x+tr)*toffset), '{0:.12f}'.format(0)))
    
    add_coeff(coe[num], x+1)
    add_coeff(0, x+1+tr)   
    add_coeff(0, x+2)
    add_coeff(0, x+3)    
    wwl.write('%s %s] \n' % ('{0:.12f}'.format((x+1)*toffset), '{0:.12f}'.format(0)))  
    return x


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
        if i == 0:
            print(kp)
        E =  kp + w*rh[i] + w*rv[i]    
        if E > 0:
            spin[i] = +1
        else:
            spin[i] = -1   
    return spin



initialize_word_bit_line_pulsewidth()    


toffset = 0.000000001
tr = 0.02
offval =0
pwidth =5




n = 256
w =3
iteration = 1





# coeff =  CoeffGen(n)
loaded_arr = np.loadtxt('icoeff.txt')

coeff = loaded_arr 
coe = coeff[:,0]

lastnumber =[]
pfnumber =[]
offval =0
pwidth =5
spin = all_zero_start(n)
sram_storage(spin)
length = len(coe)
rbl = 0
rbr = 0
drop = 1
for j in range(length):
  
    val = coe[j] * spin[j]
    if val == 1:
        rbr = rbr +drop
    elif val == -1:
        rbl = rbl +drop
 
outl = 800-rbl
outr = 800- rbr        
    
    


for i in range(len(coe)):
    x = activate_write_word_line(i,offval)
    offval = pwidth + offval + 2
for z in range(1): 
    Rh, Rv = generate_linear_random(n,iteration)

   
    
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
















y = offval +10 - offval %10

wbll.write('%s %s] \n' % ('{0:.12f}'.format((x+4)*toffset), '{0:.12f}'.format(0)))   
wblr.write('%s %s] \n' % ('{0:.12f}'.format((x+4)*toffset), '{0:.12f}'.format(0)))   
 
wwl.close()
wbll.close()
wblr.close()

pulse  = open('new_enable_256.txt', 'w')
pulse.write('simulator lang=spectre\n')

delay = y
pulse.write('vclk (CLK VSS) vsource type=pulse val0=0 val1=0.8 delay='+str(delay+5)+'n rise= 0.02n fall= 0.02n width=5n period=10n')
pulse.write('\n')

pulse.write('vs_en (EN VSS) vsource type=pulse val0=0 val1=0.8 delay='+str(delay+10)+'n rise= 0.02n fall= 0.02n width=10n period=20n')
pulse.write('\n')

# pulse.write('vspc (SPC VSS) vsource type=pulse val0=0 val1=0.8 delay=30n rise= 0.02n fall= 0.02n width=10n period=20n')
# pulse.write('\n')
 # one time mux en
pulse.write('vmux_en (MUX_EN VSS) vsource type=pulse val0=0 val1=0.8 delay='+str(delay+20)+'n rise= 0.02n fall= 0.02n width=9u period=10u')
pulse.write('\n')
pulse.write('vpc (PC VSS) vsource type=pulse val0=0 val1=0.8 delay='+str(delay+10)+'n rise= 0.02n fall= 0.02n width=15n period=20n')
pulse.write('\n')
# pulse.write('vsrl (SWL VSS) vsource type=pulse val0=0 val1=0.8 delay=30n rise= 0.02n fall= 0.02n width=10n period=20n')
# pulse.write('\n')
pulse.write('vsa_en (SA_EN VSS) vsource type=pulse val0=0 val1=0.8 delay='+str(delay+20)+'n rise= 0.02n fall= 0.02n width=10n period=20n')
pulse.write('\n')

pulse.close()
init_dff.close()