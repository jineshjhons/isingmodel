# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:42:03 2021

@author: JineshJhonsa
"""

import math
# import numpy as np
# import matplotlib.pyplot as plt


import csv


Nx=4
Ny=4


if (1):
    rv = "{0:4b}".format(1).replace('0b','').replace(' ','0')
    rh = "{0:4b}".format(1).replace('0b','').replace(' ','0')
    bias = "{0:4b}".format(0).replace('0b','').replace(' ','0')
    zero = "{0:4b}".format(0).replace('0b','').replace(' ','0')
    w_x = []
    csv_reader = csv.reader(open('coeff4x4.csv', 'r'), delimiter=',')
    cnt1 = 0
    for x in csv_reader:
        print(x)
        w_x.append([])
        for i in range(0,Ny):
            # w_x[cnt1].append(float(x[i]))
            # w_x[cnt1].append(bin(int(x[i])).replace('0b',''))
            if int(x[i]) < 0:
                w_x[cnt1].append("{0:4b}".format(16 + int(x[i])).replace('0b','').replace(' ','0'))
            else:
                w_x[cnt1].append("{0:4b}".format(int(x[i])).replace('0b','').replace(' ','0'))

        cnt1 += 1
    print(w_x)

  
# table = [[(x[0]),(x[1]),(x[2]),(x[3]),(x[4]),(x[5])] for x in csv_reader]

# f2=open(path + ,'w')
# a=x.replace(' 1\n',',1\n')
# b=a.replace(' 0\n',',0\n')
# print(table)
toffset = 0.000001
vdd = 1.2
# print('\\\\')
period = 0.000001
transition_time = 0.0000000001
# write WL
f2 = open('wl_source.txt', 'w')
f2.write('simulator lang=spectre\n')
for cnt_name in range(0,Nx*4):

    f2.write('vPC_%s (WL\\<%s\\> VSS) vsource type=pwl wave=[  \\\n'%(cnt_name, cnt_name))
    # print(cnt_name)
    # print(table[1][0])
    # print(table[1][cnt_name])
    f2.write('%s %s \\\n' % ('{0:.12f}'.format(0), '{0:.12f}'.format(float(0) * vdd)))
    f2.write('%s %s \\\n' % ('{0:.12f}'.format(toffset), '{0:.12f}'.format(float(0) * vdd)))

    f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * (cnt_name + 1) + toffset),'{0:.12f}'.format(0 * vdd)))
    f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * (cnt_name + 1) + transition_time + toffset),'{0:.12f}'.format(1 * vdd)))

    f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * (cnt_name + 2) + toffset),'{0:.12f}'.format(1 * vdd)))
    f2.write('%s %s] \n\n' % ('{0:.12f}'.format(period * (cnt_name + 2) + transition_time + toffset),'{0:.12f}'.format(0 * vdd)))

f2.close()
# print(int(10/11))
# print(int(11/11))
# print(int(12/11))
# print(22%11)
f2 = open('bl_source.txt', 'w')
f2.write('simulator lang=spectre\n')
for cnt_name in range(0,Ny*11):

    num_cim = cnt_name % 11
    num_col = int(cnt_name / 11)

    f2.write('vbl_%s (BL\\<%s\\> VSS) vsource type=pwl wave=[  \\\n'%(cnt_name, cnt_name))
    # print(cnt_name)
    # print(table[1][0])
    # print(table[1][cnt_name])
    f2.write('%s %s \\\n' % ('{0:.12f}'.format(0), '{0:.12f}'.format(float(0) * vdd)))
    f2.write('%s %s \\\n' % ('{0:.12f}'.format(toffset), '{0:.12f}'.format(float(0) * vdd)))
    data = zero
    cnt_per = 1
    f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset), '{0:.12f}'.format(float(data[0]) * vdd)))

    for cnt_wl in range(0,Nx*4-1):
        num_wl = cnt_wl%4
        num_row = int(cnt_wl/4)

        # print(data_pre)
       
        f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data[3-num_wl]) * vdd)))
        cnt_per += 1
        f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset),'{0:.12f}'.format(float(data[3-num_wl]) * vdd)))

    num_wl = (Nx-1)%4
    num_row = int((Nx-1)/4)


    f2.write('%s %s] \n\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data[3-num_wl]) * vdd)))

f2.close()
f2 = open('blb_source.txt', 'w')
f2.write('simulator lang=spectre\n')
for cnt_name in range(0,Ny*11):

    num_cim = cnt_name % 11
    num_col = int(cnt_name / 11)

    f2.write('vblb_%s (BLB\\<%s\\> VSS) vsource type=pwl wave=[  \\\n'%(cnt_name, cnt_name))
    # print(cnt_name)
    # print(table[1][0])
    # print(table[1][cnt_name])
    f2.write('%s %s \\\n' % ('{0:.12f}'.format(0), '{0:.12f}'.format(float(0) * vdd)))
    f2.write('%s %s \\\n' % ('{0:.12f}'.format(toffset), '{0:.12f}'.format(float(0) * vdd)))
    data = zero
    cnt_per = 1
    f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset), '{0:.12f}'.format((1-float(data[0])) * vdd)))

    for cnt_wl in range(0,Nx*4-1):
        num_wl = cnt_wl%4
        num_row = int(cnt_wl/4)

        # print(data_pre)
        f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data[3-num_wl]) * vdd)))

        cnt_per += 1
        f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset),'{0:.12f}'.format((1-float(data[3-num_wl])) * vdd)))

    num_wl = (Nx-1)%4
    num_row = int((Nx-1)/4)


    f2.write('%s %s] \n\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data[3-num_wl]) * vdd)))

f2.close()








# time_end = 100*4
# beta = 0.5
# f2 = open('%srandom_source.txt'%(path), 'w')
# f2.write('simulator lang=spectre\n')
#
# f2.write('vrv (RV VSS) vsource type=pwl wave=[  \\\n')
# # print(cnt_name)
# # print(table[1][0])
# # print(table[1][cnt_name])
# f2.write('%s %s \\\n' % ('{0:.12f}'.format(0), '{0:.12f}'.format(float(0) * vdd)))
# f2.write('%s %s \\\n' % ('{0:.12f}'.format(toffset), '{0:.12f}'.format(float(0) * vdd)))
# data = int(np.random.rand(1) + beta)
# cnt_per = 1
# f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset), '{0:.12f}'.format(float(data) * vdd)))
#
# for cnt_wl in range(0,time_end):
#     data = int(np.random.rand(1) + beta)
#     f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data) * vdd)))
#     cnt_per += 1
#     f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset),'{0:.12f}'.format(float(data) * vdd)))
#     beta += 0.5/time_end
# data = int(np.random.rand(1) + beta)
# f2.write('%s %s] \n\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data) * vdd)))
#
# beta = 0.5
# f2.write('vrh (RH VSS) vsource type=pwl wave=[  \\\n')
# # print(cnt_name)
# # print(table[1][0])
# # print(table[1][cnt_name])
# f2.write('%s %s \\\n' % ('{0:.12f}'.format(0), '{0:.12f}'.format(float(0) * vdd)))
# f2.write('%s %s \\\n' % ('{0:.12f}'.format(toffset), '{0:.12f}'.format(float(0) * vdd)))
# data = int(np.random.rand(1) + beta)
# cnt_per = 1
# f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset), '{0:.12f}'.format(float(data) * vdd)))
#
# for cnt_wl in range(0,time_end):
#     data = int(np.random.rand(1) + beta)
#     f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data) * vdd)))
#     cnt_per += 1
#     f2.write('%s %s  \\\n' % ('{0:.12f}'.format(period * cnt_per + toffset),'{0:.12f}'.format(float(data) * vdd)))
#     beta -= 0.5/time_end
# data = int(np.random.rand(1) + beta)
# f2.write('%s %s] \n\n' % ('{0:.12f}'.format(period * cnt_per + transition_time + toffset),'{0:.12f}'.format(float(data) * vdd)))
#
#
# f2.close()