# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:10:14 2021

@author: JineshJhonsa
"""

import numpy as np

coeffname = 'G1'
file1 = open('benchmark/'+coeffname+'.txt')
x =file1.readline()
x2 = x.split()
length =  int(x2[1])
totalnodes =  int(x2[0])
node = np.zeros([totalnodes,totalnodes])

for i in range(length):
    temp = file1.readline()
    x3 = temp.split()
    vertex = int(x3[0]) -1
    edge = int(x3[1]) -1
    weight = int(x3[2])
    node[vertex][edge] = weight
np.savetxt(coeffname +'coeff.txt',node)
    
    