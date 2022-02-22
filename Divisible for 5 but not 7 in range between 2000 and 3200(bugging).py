# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:04:17 2022

@author: Admin
"""
array=[]
a = int(input("Nhập số a: "))
if ((a<2000) or (a>3200)):
    print("Không được đâu bé ơi")
else:
    for i in range(2000,a+1):
        if((i % 7==0) and (i % 5 !=0)):
            array.append(i)
            print(array)